from django.shortcuts import render, redirect
from . import models

def index(request):
    if('book_wrong' not in request.session):
        request.session['book_wrong'] = "none"
    
    books = models.all_books()
    context = {"books": books}
    return render(request, "book.html", context)

def go_to_auther(request):
    if('author_wrong' not in request.session):
        request.session['author_wrong'] = "none"
    
    authors = models.all_authors()
    context = { "authors": authors}
    return render(request, "author.html", context)

def show_book(request, id):
    authors = models.get_authors_extend_of(id)
    book = models.get_book(id)
    context = {
        'book': book,
        'authors': authors
    }
    return render(request, 'show_book.html', context)


def show_author(request, id):
    books = models.get_books_extend_of(id)
    author = models.get_author(id)
    context = {
        'books': books,
        'author': author
    }
    return render(request, 'show_author.html', context)


def flush(request):
    request.session.flush()
    return redirect('/')


def add_book(request):
    if(request.POST['title'] == "" or request.POST['desc'] == ""):
        request.session["book_wrong"] = "block"
        return redirect('/')
    request.session["book_wrong"] = "none"
    context = {
        'title': request.POST['title'],
        'desc': request.POST['desc']
    }
    models.add_book(context)
    return redirect('/')

def add_author(request):
    if(request.POST['fname'] == "" or request.POST['lname'] == "" or request.POST['note'] == ""):
        request.session['author_wrong'] = "block"
        return redirect('authors/')
    request.session['author_wrong'] = "none"
    context = {
        'fname': request.POST['fname'],
        'lname': request.POST['lname'],
        'note': request.POST['note']
    }
    models.add_author(context)
    return redirect('authors/')

def add_book_to_author(request):
    id = request.POST['author_id']
    author = models.get_author(id)
    book = models.get_book(request.POST['new_book'])
    models.add_book_to_author(author, book)
    return redirect(f'author/{author.id}')

