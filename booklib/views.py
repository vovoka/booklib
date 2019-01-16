# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {'insert_me': 'Hello! Im a value from views.py'}
    return render(request,'booklib/index.html', context=my_dict)

def booklib_index(request):
    return HttpResponse("Booklib index page")