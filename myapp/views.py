from hashlib import new
from multiprocessing import context
from django.shortcuts import HttpResponse, render

from myapp.models import ProductModel

def index(request):
    li = ["abi","anu","aju"]
    context = {'names':li}
    return render(request,'ig.html',context=context)

def new_one(request):
    return HttpResponse("this is new")  


def products(request):
    p = ProductModel.objects.all()
    context = {'products':p}
    return render(request,'products.html',context=context)