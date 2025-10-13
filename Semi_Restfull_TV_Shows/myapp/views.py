from django.shortcuts import render, redirect
from . import models
from datetime import datetime

def all_tv_shows(request):
    all_shows = models.all_shows()
    context = {
        'shows': all_shows
    }
    return render(request, 'all_shows.html', context)

def show_tv(request, id):
    show = models.get_show(id)
    context = {
        'show': show
    }
    return render(request, 'tv_show.html', context)

def edit_show_page(request, id):
    show = models.get_show(id)
    context = {
        'show': show
    }
    return render(request, 'edit_show.html', context)

def delete_show(request):
    id = request.POST['id']
    models.remove(id)
    return redirect('/shows')

def add_new_show(request):
    return render(request, 'add_new_show.html')

def add_show(request):
    show = models.add_show(request.POST)
    return redirect(f'/shows/{show.id}')