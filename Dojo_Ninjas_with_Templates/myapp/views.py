from django.shortcuts import render, redirect
from . import models
def index(request):
    if("display_dojo" not in request.session):
        request.session['display_dojo'] = "none"
    if("display_ninja" not in request.session):
        request.session['display_ninja'] = "none"
    print(f"====================================({request.session['display_dojo']})==============================")
    dojos = models.get_all_dojos()
    context = { 'dojos' : dojos }
    return render(request, 'page.html', context)

def add_dojo(request):
    if(request.POST['name'] == "" or request.POST['city'] == "" or request.POST['state'] == ""):
        request.session['display_dojo'] = "block"
        return redirect('/')
    context = {
        'name': request.POST['name'],
        'city': request.POST['city'],
        'state': request.POST['state']
    }
    request.session['display_dojo'] = "none"
    models.add_dojo(context)
    return redirect('/')

def add_ninja(request):
    if(request.POST['fname'] == "" or request.POST['lname'] == ""):
        request.session['display_ninja'] = "block"
        return redirect('/')
    dojo = models.get_dojo(request.POST['dojo'])
    context = {
        'fname': request.POST['fname'],
        'lname': request.POST['lname'],
        'dojo': dojo
    }
    request.session['display_ninja'] = "none"
    models.add_ninja(context)
    return redirect('/')

def flush(request):
    request.session.flush()
    return redirect("/")