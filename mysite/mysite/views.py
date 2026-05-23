from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def homepage (request):
    data = {"header":"Homepage", "message": "Welcome to my site!"}
    return render(request, "homepage.html", context=data)

def about(request):
    header = "About us"
    staff = ['John', 'Rogers', 'Smith']
    director = {"name": "David Lee", "img": '/director.jpg'}
    address = ('20 W 34th st', 'New York', 'NY 10001', 'USA')
    data = {"header": header, "staff": staff, "director": director, "address": address}
    return render(request, "about.html", data)