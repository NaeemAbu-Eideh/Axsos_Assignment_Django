from django.shortcuts import render, redirect

def index(request):
    if not 'count' in request.session:
        request.session['count'] = 0 
    else:
        request.session['count']+=1
    return render(request, "page.html")

def increment(request):
    
    return render(request, "page.html")

def destroy(request):
    del request.session['count']
    return redirect("/")

def increment_by_two(request):
    if 'count' in request.session:
        request.session['count'] += 2
    return render(request, "page.html")

def increment_by_number(request):
    num = int(request.POST['increment_by_number'])
    if 'count' in request.session:
        request.session['count'] += num
    return render(request, "page.html")