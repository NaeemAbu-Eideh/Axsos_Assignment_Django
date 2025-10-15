from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
import bcrypt

def add_favorit(req):
    book = models.get_book(req.POST['book_id'])
    user = models.get_user(req.POST['user_id'])
    models.add_book_to_user_favorite(book, user)
    return {'book': book, 'user': user}

def login_signup_page(request):
    if 'user_id' in request.session:
        return redirect('/books')
    return render(request, 'login_register.html')

def register(request):
    if request.method == 'GET':
        return redirect('/')
    errors = models.User.objects.basic_validator_register(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags="register")
        return redirect('/')
    users = models.get_users_by_email(request.POST['email'])
    if len(users) > 0:
        messages.error(request, "this email is alredy used, chose another one", extra_tags="register")
        return redirect('/')
    password = request.POST['pass']
    hash_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    user = models.add_user(request.POST, hash_password)
    request.session['user_id'] = user.id
    return redirect('/books')

def all_books_page(request):
    if 'user_id' not in request.session:
        return redirect('/')
    id = request.session['user_id']
    user = models.get_user(id)
    books = models.all_books()
    context ={
        'user': user,
        'books': books
    }
    return render(request, 'all_books.html', context)

def signin(request):
    if request.method == 'GET':
        return redirect('/')
    errors = models.User.objects.basic_validator_login(request.POST)
    if len(errors) != 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags="login")
        return redirect('/')
    users = models.get_users_by_email(request.POST['email'])
    if len(users) == 0:
        messages.error(request, "email not found", extra_tags="login")
        return redirect('/')
    user = models.get_user_by_email(request.POST['email'])
    password = request.POST['pass']
    chack = bcrypt.checkpw(password.encode() ,user.password.encode())
    if chack == False:
        messages.error(request, "email or passwoer not found, please re-enter it", extra_tags="login")
        return redirect('/')
    request.session['user_id'] = user.id
    return redirect('/books')

def logout(request):
    if request.method == 'GET':
        return redirect('/')
    del request.session['user_id']
    return redirect('/')

def add_favorite_bbok(request):
    if request.method == "GET":
        return redirect('/books')
    errors = models.Book.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags="book")
        return redirect('/books')
    user_id = request.POST['user_id']
    user = models.get_user(user_id)
    book = models.add_book(request.POST, user)
    models.add_book_to_user_favorite(book, user)
    return redirect('/books')

def flush(request):
    request.session.flush()
    return redirect('/')

def add_to_your_favoriets(request):
    if request.method == "GET":
        return redirect('/books')
    add_favorit(request)
    return redirect('/books')

def add_to_your_favoriets_in_info(request):
    if request.method == "GET":
        return redirect('/books')
    context = add_favorit(request)
    book = context['book']
    return redirect(f'/books/{book.id}')

def show_book_details(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    
    book = models.get_book(id)
    user = models.get_user(request.session['user_id'])
    context = {
        'book': book,
        'user': user
    }
    user_id = book.uploaded_by.id
    if user_id == user.id:
        return render(request, 'edit_book.html', context)
    return render(request, 'book_details.html', context)

def delete_book(request):
    if request.method == "GET":
        return redirect('/books')
    id  = request.POST["id_for_book"]
    book = models.get_book(id)
    users = book.users_who_likes.all()
    for user in users:
        book.users_who_likes.remove(user)
    book.delete()
    return redirect('/books')

def update_book_details(request):
    if request.method == "GET":
        return redirect('/books')
    id = request.POST['book_id']
    book = models.get_book(id)
    book.title = request.POST['title']
    book.description = request.POST['desc']
    book.save()
    return redirect(f'/books/{book.id}')

def un_favorite(request):
    if request.method == "GET":
        return redirect('/books')
    book_id = request.POST['book_id']
    user_id = request.session['user_id']
    user = models.get_user(user_id)
    book = models.get_book(book_id)
    models.remove_user_from_favorite(book, user)
    return redirect(f'/books/{book.id}')