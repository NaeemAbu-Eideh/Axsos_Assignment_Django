from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
import myapp.models as user_models

def main_page(request):
    if 'account_user' in request.session:
        messages_desc = models.get_all_messages()
        context = {
            'messages_desc': messages_desc
        }
        return render(request, "posts.html", context)
    return render(request, 'go_to_login_signup.html')

def logout(request):
    if 'account_user' in request.session:
        del request.session['account_user']
    return redirect('/')

def flush(request):
    request.session.flush()
    return redirect('/')

def post_message(request):
    errors = models.Message.objects.basic_validator(request.POST)
    if(len(errors) > 0):
        for key, value in errors.items():
            messages.error(request, value, extra_tags="message")
        return redirect('/')
    models.add_message(request.POST, request.session['account_user'])
    return redirect('/')

def go_to_comment_page(request):
    if 'account_user' in request.session:
        messages_desc = models.get_all_messages()
        context = {
            'messages_desc': messages_desc
        }
        return render(request, "comments.html", context)
    return redirect('/')

def post_comment(request):
    errors = models.Comment.objects.basic_validator(request.POST)
    if(len(errors) > 0):
        for key, value in errors.items():
            messages.error(request, value, extra_tags="comment")
        return redirect('/wall')
    id = request.POST['id']
    models.add_comment(request.POST, id)
    return redirect('/wall')