from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book = models.ManyToManyField(Book, related_name='authors')
    notes = models.TextField()


def add_book(book):
    Book.objects.create(title = book['title'], desc = book['desc'])

def add_author(author):
    Author.objects.create(first_name = author['fname'], last_name = author['lname'], notes = author['note'])

def get_book(book_id):
    return Book.objects.get(id = book_id)

def get_author(author_id):
    return Author.objects.get(id = author_id)

def all_books():
    return Book.objects.all()

def all_authors():
    return Author.objects.all()

def all_book_authors(book):
    return book.authors.all()

def all_author_books(author):
    return author.book.all()

def add_book_to_author(author, book):
    author.book.add(book)

def add_author_to_book(book, author):
    book.authors.add(author)

def get_books_extend_of(id):
    author = get_author(id)
    return Book.objects.exclude(authors = author.id)

def get_authors_extend_of(id):
    book = get_book(id)
    return Author.objects.exclude(book = book.id)