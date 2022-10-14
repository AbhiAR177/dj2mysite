from hashlib import new
from django.shortcuts import HttpResponse, render

def index(request):
    return HttpResponse(['string',1,2,3,4])

def new_one(request):
    return HttpResponse("this is new")