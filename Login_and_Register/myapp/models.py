from django.db import models
import re
# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, request):
        errors = {}
        emails_pattern = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if('fname' in request and request['fname'] == ''):
            errors['fname'] = "please fill the First Name"
        
        elif('fname' in request and len(request['fname']) < 2):
            errors['fname'] = "First Name shuld have at least 2 chars"
        
        if('lname' in request and request['lname'] == ''):
            errors['lname'] = "please fill the Last Name"
            
        elif('lname' in request and len(request['lname']) < 2):
            errors['lname'] = "Last Name shuld have at least 2 chars"
            
        if('email' in request and request['email'] == ''):
            errors['email'] = "please fill the email"
        
        elif('email' in request and not emails_pattern.match(request['email'])):
            errors['email'] = "email does not match"
        
        if ('pass' in request and request['pass'] == ''):
            errors['pass'] = "please fill the Password"
        
        elif ('pass' in request and len(request['pass']) < 8):
            errors['pass'] = "password shod have at least 8 characters"
        
        if ('cpass' in request and request['cpass'] == ''):
            errors['cpass'] = "please fill the Confirm Password"
        
        if ('cpass' in request and 'pass' in request and request['pass'] != request['cpass']):
            errors['match'] = "confirm password must be equal password"
        return errors
    def basic_validator_login(self, request):
        errors = {}
        emails_pattern = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if('email' in request and request['email'] == ''):
            errors['email'] = "please fill the email"
        
        elif('email' in request and not emails_pattern.match(request['email'])):
            errors['email'] = "email does not match"
        
        if ('pass' in request and request['pass'] == ''):
            errors['pass'] = "please fill the Password"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Password = models.TextField()
    objects = UserManager()
    
def add_user(context, password):
    User.objects.create(first_name = context['fname'], last_name = context['lname'], Email = context['email'], Password = password)

def get_user(email):
    return User.objects.get(Email = email)
