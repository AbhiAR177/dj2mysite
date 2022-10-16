from hashlib import new
from multiprocessing import context
from django.shortcuts import HttpResponse, render

from myapp.models import ProductModel
from django.db.models import Q

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

def product_details(request,id):
    p = ProductModel.objects.get(id=id)
    context={'p':p}
    return render(request,'product_details.html',context=context)

def add_product(request):
    p = ProductModel(name = "SONY Bravia 4K UHD TV")
    p.price = 90000.0
    p.desc = "This is a 75 inch hd tv"
    
    p.save()
    return HttpResponse(p)