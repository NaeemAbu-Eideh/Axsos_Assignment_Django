from django.shortcuts import render, redirect
from . import models
from datetime import datetime


def add_show(request):
    return render(request, 'add_new_show.html')

def edit_show(request, id):
    request.session['edit_id'] = id
    return render(request, 'edit_show.html')

def all_shows(request):
    shows = models.all_shows()
    context = {
        'shows': shows
    }
    return render(request, 'all_shows.html', context)

def tv_show(request, id):
    show = models.get_show(id)
    context = {
        'show': show
    }
    return render(request, 'tv_show.html', context)

def insert_show(request):
    context = {
        'title': request.POST['title'],
        'network': request.POST['network'],
        'date': request.POST['date'],
        'desc': request.POST['desc']
    }
    models.add_show(context)
    return redirect('shows/2/')

def update_show(request):
    context = {
        'title' : request.POST['title'],
        'date' : request.POST['date'],
        'network' : request.POST['network'],
        'desc' : request.POST['desc']
    }
    id = request.session['edit_id']
    models.update_title(id, context['title'])
    models.update_network(id, context['network'])
    models.update_release_date(id, context['date'])
    models.update_description(id, context['desc'])
    return redirect(f'shows/{{id}}/')