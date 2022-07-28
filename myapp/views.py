from django.http import HttpResponse
from django.shortcuts import render
import psutil
import platform
from datetime import datetime
import calendar
from calendar import HTMLCalendar 

# Create your views here.
def index(request):
    return HttpResponse("This is my app")

def date_time(request):
    x = datetime.now()
    html1="<html><body><b> current date and time is: %s </b></body></html>" % x 
    return HttpResponse(html1)

def sys_info(request):
    uname = platform.uname()
    return HttpResponse(f"System: {uname.system}")
    return HttpResponse(f"Node Name: {uname.node}")
    return HttpResponse(f"Node Name: {uname.node}")
    return HttpResponse(f"Release: {uname.release}")
    return HttpResponse(f"Version: {uname.version}")
    return HttpResponse(f"Machine: {uname.machine}")
    return HttpResponse(f"Processor: {uname.processor}")

def calendar(request, year, month):
    name = "nimra"
    month = month.capitalize()

    #convert month from name to number
    
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(year,month_number)

    return render(request, 'calendar.html', {
        "name": name,
        "year": year,
        "month": month,
       
        "cal": cal,
        })