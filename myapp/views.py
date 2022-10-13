from django.shortcuts import HttpResponse, render

def index(request):
    return HttpResponse(['string',1,2,3,4])
