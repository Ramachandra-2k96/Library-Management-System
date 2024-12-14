from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name="index.html"),name='home'),
    
    path('books/', views.book_list_view, name='book_list'),
    
    path('users/login/', views.login_view, name='login'),
    path('users/signup/', views.signup_view, name='signup'),
    path('reader/profile/', views.profile_view, name='profile'),
    
    path('users/logout/', views.logout_view, name='logout'),
    
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
    
    
    path('books/borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('books/return/<int:borrowed_id>/', views.return_book, name='return_book'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
