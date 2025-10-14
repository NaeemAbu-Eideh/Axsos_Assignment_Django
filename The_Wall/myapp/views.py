from django.shortcuts import render, redirect
from django.contrib import messages
from . import models
import bcrypt

def login_signup(request):
    return render(request, 'login_signup.html')


def register(request):
    errors = models.User.objects.basic_validator(request.POST)
    if len(errors) != 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags="signup")
        return redirect('/login')
    
    password = request.POST['pass']
    hash1 = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    models.add_user(request.POST, hash1)
    request.session['account_user'] = request.POST
    return redirect('/')

def login(request):
    print("naeem abueidfojefsfgnkjljgrgknl;")
    errors = models.User.objects.basic_validator_login(request.POST)
    if len(errors) != 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags="login")
        return redirect('/login')
    
    user = models.get_user(request.POST['email'])
    password = request.POST['pass']
    chack = bcrypt.checkpw(password.encode() ,user.Password.encode())
    if chack == False:
        messages.error(request, "email or passwoer not found, please re-enter it", extra_tags="login")
        return redirect('/login')
    
    context = {
        'id': user.id,
        'fname' : user.first_name,
        'lname' : user.last_name,
        'email' : user.Email,
        'pass' : user.Password,
    }
    request.session['account_user'] = context
    return redirect('/')

def flush(request):
    request.session.flush()
    return redirect('/login')

