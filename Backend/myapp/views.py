from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile, Book, BorrowedBook
from django.urls import reverse
from django.http import HttpResponsePermanentRedirect
from django.db.models import Q

def signup_view(request):
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
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return HttpResponsePermanentRedirect(reverse('login'))

def book_list_view(request):
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
    if request.method == 'POST':
        try:
            book = Book.objects.get(id=book_id)
            if not BorrowedBook.objects.filter(book=book, reader=request.user, is_returned=False).exists():
                BorrowedBook.objects.create(
                    book=book,
                    reader=request.user
                )
                messages.success(request, f'Successfully borrowed "{book.title}"')
            else:
                messages.error(request, 'You have already borrowed this book')
        except Book.DoesNotExist:
            messages.error(request, 'Book not found')
    return redirect('book_list')

@login_required
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        
        if title and description and image:
            try:
                book = Book.objects.create(
                    title=title,
                    description=description,
                    image=image,
                    author=request.user
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
    try:
        book = Book.objects.get(id=book_id)
        
        if book.author != request.user:
            messages.error(request, 'You can only edit your own books')
            return redirect('book_list')
            
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            image = request.FILES.get('image')
            
            if title and description:
                book.title = title
                book.description = description
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
