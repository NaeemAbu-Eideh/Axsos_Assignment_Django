from django.shortcuts import render, redirect
import random

def index(request):
    request.session['background_color'] = "red"
    request.session['display_result'] = "none"
    request.session['result'] = ""
    request.session['diaplay_button'] = "none"
    request.session['random'] = random.randint(1,100)
    return render(request, "index.html")

def input(request):
    num = int(request.POST['number'])
    if(num > request.session['random']):
        request.session['background_color'] = "red"
        request.session['display_result'] = "block"
        request.session['result'] = "Too hight!"
        
    elif (num < request.session['random']):
        request.session['background_color'] = "red"
        request.session['display_result'] = "block"
        request.session['result'] = "Too low!"
        
    else:
        request.session['background_color'] = "green"
        request.session['display_result'] = "block"
        request.session['result'] = f"{num} was the number!"
        request.session['diaplay_button'] = "block"
    return redirect('newPage/')
    
def newPage(request):
    return render(request, "index.html")

def play_again(request):
    return redirect("/")