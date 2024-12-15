# 📚 Digital Library

<div align="center">

![Digital Library Logo](image.png)

A modern, feature-rich digital library management system built with Django and TailwindCSS.

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-5.0+-green.svg)](https://www.djangoproject.com/)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.0+-blueviolet.svg)](https://tailwindcss.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

## ✨ Features

### 👥 User Management
- **Dual User Types**: Support for both readers and authors
- **Profile Management**: Customizable user profiles with avatars
- **Authentication**: Secure login with remember-me functionality
- **Account Management**: Self-service account updates and deletion

### 📖 Book Management
- **Book Catalog**: Comprehensive book listing with search functionality
- **Real-time Search**: Dynamic search without page reloads
- **Book Details**: Rich book information including cover images
- **Copy Management**: Track multiple copies of each book

### 📱 User Interface
- **Modern Design**: Sleek, responsive interface with glass-morphism effects
- **Dark Theme**: Eye-friendly dark mode by default
- **Animations**: Smooth transitions and loading animations
- **Mobile Responsive**: Fully responsive design for all devices

### 📚 Library Functions
- **Book Borrowing**: Easy book borrowing system for readers
- **Author Dashboard**: Special features for authors to manage their books
- **Copy Tracking**: Real-time tracking of available book copies
- **Return Management**: Streamlined book return process

## 🚀 Getting Started

### Prerequisites
- Python 3.12 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. Clone the repository
```bash
git clone https://github.com/Ramachandra-2k96/Library-Management-System.git
```
2. Navigate to the project directory
```bash
cd Library-Management-System
```
3. Create a virtual environment
```bash
python -m venv venv
```
4. Activate the virtual environment
```bash
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
5. Install dependencies
```bash
pip install -r requirements.txt
```
6. Run migrations
```bash
python manage.py migrate
```
7. Start the development server
```bash
python manage.py runserver
```

8. Access the application

Visit `http://localhost:8000` to see the application in action!

## 🎯 Usage

### For Readers
- Create an account as a reader
- Browse the book catalog
- Search for specific books
- Borrow available books
- Track borrowed books
- Return books when finished

### For Authors
- Register as an author
- Add new books to the library
- Manage book information
- Track copies of your books
- Update book details
- Remove books from the catalog

## 🛠️ Tech Stack

- **Backend**: Django 5.0+
- **Frontend**: TailwindCSS 3.0+
- **Database**: SQLite (default), PostgreSQL (production)
- **Authentication**: Django Authentication System
- **File Storage**: Django File Storage
- **Animations**: GSAP, Animate.css
- **Icons**: Heroicons

## Testing Video
[Testing Video](https://github.com/Ramachandra-2k96/Library-Management-System/blob/main/0000-2078.mp4)


## 📝 Project Structure
```
digital-library/
├── Backend/
│   ├── myapp/
│   │   ├── templates/
│   │   ├── static/
│   │   ├── models.py
│   │   ├── forms.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── media/
│   │   ├── bookimages/
│   │   └── profile_pictures/
│   ├── Backend/
│   │   └── settings.py
│   ├── manage.py
│   └── requirements.txt
```
## 📧 Contact

Ramachandra Udupa - [@ramachandra_udupa](https://twitter.com/ramachandra_udupa) - ramachandraudupa2000@gmail.com

Project Link: [https://github.com/Ramachandra-2k96/Library-Management-System](https://github.com/Ramachandra-2k96/Library-Management-System)

---

<div align="center">
Made with ❤️ by Ramachandra Udupa
</div>
