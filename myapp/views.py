from hashlib import new
from multiprocessing import context
from unicodedata import name
from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth.decorators import login_required

from myapp.models import ProductModel
from django.db.models import Q

def index(request):
    li = ["abi","anu","aju"]
    context = {'names':li}
    return render(request,'ig.html',context=context)

def new_one(request):
    return HttpResponse("this is new")  

@login_required
def products(request):
    p = ProductModel.objects.all()
    context = {'products':p}
    return render(request,'products.html',context=context)

def product_details(request,id):
    p = ProductModel.objects.get(id=id)
    context={'p':p}
    return render(request,'product_details.html',context=context)

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']
    
        p = ProductModel(name=name,price=price,desc=desc,image=image)
        p.save() 
        
        
        return redirect('/myapp/products')
    
    return render(request,'add_product.html')



def update_product(request,id):
    p = ProductModel.objects.get(id=id)
    context={'p':p}
    
    
    if request.method == 'POST':
        p.name = request.POST.get('name')
        p.price = request.POST.get('price')
        p.desc = request.POST.get('desc')
        
        try:
            p.image = request.FILES['upload']
        except:
            pass    
    
        # p = ProductModel(name=name,price=price,desc=desc,image=image)
        p.save() 
        
        
        return redirect('/myapp/products')
    
    return render(request,'update_product.html',context=context)

def delete_product(request,id):
    p = ProductModel.objects.get(id=id)
    context={'p':p}
    
    
    if request.method == 'POST':
        
        p.delete()
        
        
        return redirect('/myapp/products')
    
    return render(request,'delete_product.html',context=context)