from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
from datetime import datetime
from zoneinfo import ZoneInfo

def index(request):
    palestine_time = datetime.now(ZoneInfo("Asia/Jerusalem"))
    context = {
        "time": palestine_time.strftime("%b %d , %Y %I:%M %p")
    }
    return render(request,'page.html', context)