from django.http import HttpResponse
import psutil
import platform
from datetime import datetime

# Create your views here.
def index(request):
    return HttpResponse("This is my app")

def date_time(request):
    x = datetime.datetime.now()
    html1="<html><body><b> current date and time is: %s </b></body></html>" % x 
    return HttpResponse(html1)

def sys_info(request):
    uname = platform.uname()
    return HttpResponse(f"System: {uname.system} \nNode: {uname.node} \nRelease: {uname.release} \nVersion: {uname.version} \nMachine: {uname.machine} \nProcessor: {uname.processor}")

def calendar(request):
    return HttpResponse("This is calendar page")
