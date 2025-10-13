from django.shortcuts import render, redirect
from django.contrib import messages
from . import models
import bcrypt

def login_signup(request):
    if 'signup_display' not in request.session:
        request.session['signup_display'] = "none"
    if 'login_display' not in request.session:
        request.session['login_display'] = "none"
    return render(request, 'login_signup.html')

def success(request):
    return render(request, 'sucsess.html')
def register(request):
    errors = models.User.objects.basic_validator(request.POST)
    if len(errors) != 0:
        request.session['signup_display'] = "block"
        request.session['login_display'] = "none"
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    request.session['signup_display'] = "none"
    request.session['login_display'] = "none"
    password = request.POST['pass']
    hash1 = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    models.add_user(request.POST, hash1)
    request.session['account_user'] = request.POST
    return redirect('success/')

def login(request):
    errors = models.User.objects.basic_validator_login(request.POST)
    if len(errors) != 0:
        request.session['signup_display'] = "none"
        request.session['login_display'] = "block"
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    request.session['signup_display'] = "none"
    request.session['login_display'] = "none"
    user = models.get_user(request.POST['email'])
    password = request.POST['pass']
    chack = bcrypt.checkpw(password.encode() ,user.Password.encode())
    if chack == False:
        request.session['signup_display'] = "none"
        request.session['login_display'] = "block"
        messages.error(request, "email or passwoer not found, please re-enter it")
        return redirect('/')
    request.session['signup_display'] = "none"
    request.session['login_display'] = "none"
    context = {
        'fname' : user.first_name,
        'lname' : user.last_name,
        'email' : user.Email,
        'pass' : user.Password,
    }
    request.session['account_user'] = context
    return redirect('success/')

def flush(request):
    request.session.flush()
    return redirect('/')

def logout(request):
    if 'account_user' in request.session:
        del request.session['account_user']
    return redirect('/')