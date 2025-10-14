from django.shortcuts import render, redirect
from . import models
import re
from django.contrib import messages
def add_show_courses(request):
    courses = models.get_all_courses()
    context = {
        'courses': courses
    }
    return render(request, 'add_show_courses.html', context)

def add_course(request):
    errors = models.Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    models.add_course(request.POST)
    return redirect('/')

def destroy_course(request, id):
    course = models.get_course(id)
    context = {
        'course': course
    }
    return render(request, 'remove_course.html', context)

def remove_course(request):
    models.delete_course(request.POST['id'])
    return redirect('/')


