from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.index, name="myapp"),
    path("date_time", views.date_time, name="date_time"),
    path("sys_info", views.sys_info, name="sys_info"),
    path("calendar", views.calendar, name="calendar"),
]
