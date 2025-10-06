from django.shortcuts import render, redirect
from .models import *
def index(request):
    if  'display' not in request.session:
        request.session['display'] = "none"
    records = User.get_all_records()
    context = {
        "records": records
    }
    return render(request, 'page.html', context)

def add_user(request):
    if(request.POST['fname'] == "" or request.POST['lname'] == "" or request.POST['email'] == "" or request.POST['age'] == ""):
        request.session['display'] = "block"
        return redirect("/")
    context = {
        'fname': request.POST['fname'],
        'lname': request.POST['lname'],
        'email': request.POST['email'],
        'age': int(request.POST['age']),
    }
    request.session['display'] = "none"
    User.create_record(context)
    return redirect("/")

def error(request):
    return render(request, 'page.html')

def dell(request):
    request.session.flush()
    return redirect('/')