# from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect  
# from vadmin.forms import UserForm  
# from vadmin.models import User  
from django.shortcuts import render
from django.urls import path
# from .models import User
from .models import Product

def my_view(request):
    return render(request, 'index.html')

def product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product.html', context)

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

def User(request):
    return render(request, 'users.html')
    # User = User.objects.all()
    # return render(request, 'users.html', {'users': User})
# 
def login(request):
    # if request.method == 'POST':
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     user = authenticate(email=email, password=password)
    #     if user is not None:
    #         auth_login(request, user)
    #         return render(request, 'index.html')
    #     else:
    #         pass
    return render(request, 'login.html')


def register(request):
    # if request.method == "POST":  
    #     form = UserForm(request.POST)  
    #     if form.is_valid():  
    #         try:  
    #             form.save()  
    #             return redirect('/home')  
    #         except:  
    #             pass  
    # else:  
    #     form = UserForm()  
    # return render(request, 'register.html')
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     phone = request.POST.get('phone')
    #     address = request.POST.get('address')
    #     city = request.POST.get('city')
    #     state = request.POST.get('state')
    #     zip = request.POST.get('zip')
    #     country = request.POST.get('country')
        
    #     # Create a new user object and save it to the database
    #     new_user = User(name=name, email=email, password=password, phone=phone, address=address, city=city, state=state, zip=zip, country=country)
    #     new_user.save()
        
    #     # Redirect to a success page or display a success message
    #     return render(request, 'index.html')
    # # Render the registration form
    return render(request, 'register.html')