from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator_register(self, post):
        errors = {}
        email_pattern = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if post['fname'] == '':
            errors['fname'] = "First Name is empty, fill it"
        
        elif len(post['fname']) < 2:
            errors['fname'] = "Firat Name must have at least 2 characters"
        
        if post['lname'] == '':
            errors['lname'] = "Last Name is empty, fill it"
        
        elif len(post['lname']) < 2:
            errors['lname'] = "Last Name must have at least 2 characters"
        
        if post['email'] == '':
            errors['email'] = "email is empty, fill it"
        
        elif not email_pattern.match(post['email']):
            errors['email'] = "email does not match"
        
        if post['pass'] == '':
            errors['pass'] = "Password is empty, fill it"
        
        elif len(post['pass']) < 8:
            errors['pass'] = "Password must have at least 8 characters"
        
        if post['cpass'] == '':
            errors['cpass'] = "Confirmd Password is empty, fill it"
        
        elif post['pass'] != post['cpass']:
            errors['pass'] = "passwords does not match"
        
        return errors
    
    def basic_validator_login(self, post):
        errors = {}
        email_pattern = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if post['email'] == '':
            errors['email'] = "email is empty, fill it"
        
        elif not email_pattern.match(post['email']):
            errors['email'] = "email does not match"
        
        if post['pass'] == '':
            errors['pass'] = "Password is empty, fill it"
        
        return errors

class BookManager(models.Manager):
    def basic_validator(self, post):
        errors = {}
        if( post['title'] == ''):
            errors['title'] = "Book Title is empty, fill it"
        
        if post['desc'] == '':
            errors['desc'] = "Book description is empty, fill it"
        
        elif len(post['desc']) < 5:
            errors['desc'] = "Book description must have at least 5 characters"
        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.TextField()
    email = models.CharField(max_length=40, unique=True)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_likes = models.ManyToManyField(User, related_name="liked_books")
    objects = BookManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def add_user(post, password):
    return User.objects.create(first_name = post['fname'], last_name = post['lname'], email = post['email'], password = password)

def get_user_by_email(email):
    return User.objects.get(email = email)

def get_user(id):
    return User.objects.get(id = id)

def all_books():
    return Book.objects.all()

def add_book(post, user):
    return Book.objects.create(title = post['title'], description = post['desc'], uploaded_by = user)

def add_book_to_user_favorite(book, user):
    book.users_who_likes.add(user)

def get_book(id):
    return Book.objects.get(id = id)

def remove_book_from_favorite(user, book):
    user.liked_books.reomve(book)

def remove_user_from_favorite(book, user):
    book.users_who_likes.remove(user)

def get_users_by_email(email):
    return User.objects.filter(email = email)