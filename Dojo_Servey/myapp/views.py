from django.shortcuts import render, redirect

def index(request):
    return render(request, "sign_information.html")

def result(requset):
    dic = {
        "name": requset.POST['name'],
        "language": requset.POST['language'],
        "location": requset.POST['location'],
        "comment": requset.POST['comment']
    }
    return render(requset, "show_information.html", dic)
