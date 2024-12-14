from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from .models import Book, BorrowedBook
from django.urls import reverse
from django.http import HttpResponsePermanentRedirect
from django.db.models import Q
from django.utils import timezone

def signup_view(request):
    """
    View for user signup.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_type = request.POST.get('user_type')

        # Validation checks
        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return redirect('signup')

        # Create new user
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            
            # Set the user type in the profile
            user.userprofile.user_type = user_type
            user.userprofile.save()
            
            # Log the user in after signup
            auth_login(request, user)
            messages.success(request, 'Account created successfully!')
            return HttpResponsePermanentRedirect(reverse('profile'))
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
            return redirect('signup')

    return render(request, 'signup.html')

def login_view(request):
    """
    View for user login.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me') == 'on'

        try:
            # Get username from email
            user = User.objects.get(email=email)
            # Authenticate using username
            authenticated_user = authenticate(request, username=user.username, password=password)
            
            if authenticated_user is not None:
                auth_login(request, authenticated_user)
                
                # Handle remember me functionality
                if remember_me:
                    # Set session expiry to 15 days
                    request.session.set_expiry(1296000)  # 15 days in seconds
                else:
                    # Session expires when browser closes
                    request.session.set_expiry(0)
                
                messages.success(request, 'Login successful!')
                return redirect('profile')
            else:
                messages.error(request, 'Invalid credentials!')
        except User.DoesNotExist:
            messages.error(request, 'No account found with this email!')
        except Exception as e:
            messages.error(request, f'Error during login: {str(e)}')

    return render(request, 'login.html')

@login_required
def profile_view(request):
    """
    View for user profile.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    user_profile = request.user.userprofile
    context = {
        'user_profile': user_profile,
    }

    if user_profile.user_type == 'author':
        # Get books authored by the user
        books = Book.objects.filter(author=request.user)
        context['books'] = books
    else:
        # Get books borrowed by the user
        borrowed_books = BorrowedBook.objects.filter(
            reader=request.user,
            is_returned=False
        ).select_related('book')
        context['borrowed_books'] = borrowed_books

    return render(request, 'profile.html', context)

def logout_view(request):
    """
    View for user logout.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return HttpResponsePermanentRedirect(reverse('login'))

def book_list_view(request):
    """
    View for book list.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    query = request.GET.get('search', '')
    books = Book.objects.all().select_related('author').order_by('-created_at')
    
    if query:
        books = books.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(author__username__icontains=query)
        )
    
    context = {
        'books': books[:100],  # Limit to 100 books
        'query': query,
        'user_type': request.user.userprofile.user_type if request.user.is_authenticated else 'guest'
    }
    return render(request, 'books.html', context)

@login_required
def borrow_book(request, book_id):
    """
    View for borrowing a book.

    Args:
        request (HttpRequest): The HTTP request object.
        book_id (int): The ID of the book to borrow.

    Returns:
        HttpResponse: The HTTP response object.
    """
    if request.method == 'POST':
        try:
            book = Book.objects.get(id=book_id)
            # Check if user has already borrowed this book
            if BorrowedBook.objects.filter(book=book, reader=request.user, is_returned=False).exists():
                messages.error(request, 'You have already borrowed this book')
                return redirect('book_list')
            
            # Check if copies are available
            if book.num_of_copies <= 0:
                messages.error(request, 'No copies available for borrowing')
                return redirect('book_list')
            
            # Create borrow record and decrease number of copies
            BorrowedBook.objects.create(
                book=book,
                reader=request.user
            )
            book.num_of_copies -= 1
            book.save()
            messages.success(request, f'Successfully borrowed "{book.title}"')
            
        except Book.DoesNotExist:
            messages.error(request, 'Book not found')
    return redirect('book_list')

@login_required
def return_book(request, borrowed_id):
    """
    View for returning a borrowed book.

    Args:
        request (HttpRequest): The HTTP request object.
        borrowed_id (int): The ID of the borrowed book to return.

    Returns:
        HttpResponse: The HTTP response object.
    """
    if request.method == 'POST':
        try:
            borrowed = BorrowedBook.objects.get(id=borrowed_id, reader=request.user, is_returned=False)
            borrowed.is_returned = True
            borrowed.return_date = timezone.now()
            borrowed.save()
            
            # Increase the number of copies
            book = borrowed.book
            book.num_of_copies += 1
            book.save()
            
            messages.success(request, f'Successfully returned "{book.title}"')
        except BorrowedBook.DoesNotExist:
            messages.error(request, 'Borrowed book record not found')
    return redirect('profile')

@login_required
def add_book(request):
    """
    View for adding a book.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        num_of_copies = request.POST.get('num_of_copies', 1)
        
        if title and description and image:
            try:
                book = Book.objects.create(
                    title=title,
                    description=description,
                    image=image,
                    author=request.user,
                    num_of_copies=num_of_copies
                )
                messages.success(request, f'Successfully added book "{title}"')
                return redirect('book_list')
            except Exception as e:
                messages.error(request, f'Error adding book: {str(e)}')
        else:
            messages.error(request, 'All fields are required')
    
    return render(request, 'add_book.html')

@login_required
def edit_book(request, book_id):
    """
    View for editing a book.

    Args:
        request (HttpRequest): The HTTP request object.
        book_id (int): The ID of the book to edit.

    Returns:
        HttpResponse: The HTTP response object.
    """
    try:
        book = Book.objects.get(id=book_id)
        
        if book.author != request.user:
            messages.error(request, 'You can only edit your own books')
            return redirect('book_list')
            
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            image = request.FILES.get('image')
            num_of_copies = request.POST.get('num_of_copies', book.num_of_copies)
            
            if title and description:
                book.title = title
                book.description = description
                book.num_of_copies = num_of_copies
                if image:
                    book.image = image
                book.save()
                messages.success(request, f'Successfully updated "{title}"')
                return redirect('book_list')
            else:
                messages.error(request, 'Title and description are required')
                
        context = {
            'book': book
        }
        return render(request, 'edit_book.html', context)
        
    except Book.DoesNotExist:
        messages.error(request, 'Book not found')
        return redirect('book_list')

@login_required
def delete_book(request, book_id):
    """
    View for deleting a book.

    Args:
        request (HttpRequest): The HTTP request object.
        book_id (int): The ID of the book to delete.

    Returns:
        HttpResponse: The HTTP response object.
    """
    try:
        book = Book.objects.get(id=book_id)
        
        # Check if user is the author
        if book.author != request.user:
            messages.error(request, 'You can only delete your own books')
            return redirect('book_list')
            
        if request.method == 'POST':
            book_title = book.title
            book.delete()
            messages.success(request, f'Successfully deleted "{book_title}"')
        
        return redirect('book_list')
        
    except Book.DoesNotExist:
        messages.error(request, 'Book not found')
        return redirect('book_list')
