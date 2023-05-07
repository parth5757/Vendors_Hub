# from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from vadmin.forms import ProductForm, CategoryForm
# from vadmin.models import User  
from django.shortcuts import render
from django.urls import path
from .models import *
import re

def my_view(request):
    return render(request, 'index.html')

def category(request):
    categorys = Category.objects.all()
    context = {'categorys': categorys}
    return render(request, 'category.html', context)

def product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product.html', context)

def add_category(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']        
        category = Category(category_name=name, category_description=description)
        category.save()
        return redirect('category')
    else:
        return render(request, 'add_category.html')
    
def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        # image = request.POST['image']
        category = request.POST['category']
        quantity = request.POST['quantity']
        brand = request.POST['brand']
        stock = request.POST['stock']
        discount = request.POST['discount']
        product = Product(name=name, price=price, description=description, category=category, quantity=quantity, brand=brand, stock=stock, discount=discount)
        product.save()
        return redirect('product')
    else:
        return render(request, 'add_product.html')
    

def delete_product(request, id):
    product = Product.objects.get(p_id=id)    
    product.delete()
    return redirect('product')

def update_product(request, id):
    product = Product.objects.get(p_id=id)
    form = ProductForm(instance=product)
    context = {'product': product, 'form': form}

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product')

    return render(request, 'update_product.html', context)

def User(request):
    return render(request, 'users.html')
    # User = User.objects.all()
    # return render(request, 'users.html', {'users': User})
# 

    
def error(request, undefined_route):
    return render(request, 'error_400.html')


    
def delete_category(request, id):
    category = Category.objects.get(c_id=id)    
    category.delete()
    return redirect('category')

def update_category(request, id):
    category = Category.objects.get(c_id=id)
    form = CategoryForm(instance=category)
    context = {'category': category, 'form': form}
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category')

    return render(request, 'update_category.html', context)

def about(request):
    return render(request, 'about.html')


