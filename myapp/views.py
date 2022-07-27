from django.shortcuts import render, HttpResponse
from datetime import datetime
x=datetime.now()

# Create your views here.
def index(request):
    return HttpResponse("This is my app")

def date_time(request):
    return HttpResponse({"Today's date and time is" : x})

def sys_info(request):
    return HttpResponse("This is System Information page")

def calendar(request):
    return HttpResponse("This is calendar page")