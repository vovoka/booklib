from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def booklib_index(request):
    return HttpResponse("Booklib index page")

def index(request):
    return HttpResponse("Hello world")