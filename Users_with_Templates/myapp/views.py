from django.shortcuts import render, redirect
from .models import *
def index(request):
    records = User.get_all_records()
    context = {
        "records": records
    }
    return render(request, 'page.html', context)

def add_user(request):
    context = {
        'fname': request.POST['fname'],
        'lname': request.POST['lname'],
        'email': request.POST['email'],
        'age': request.POST['age'],
    }
    User.create_record(context)
    return redirect("/")

def error(request):
    return render(request, 'page.html')