from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect  
# from vadmin.forms import UserForm  
# from vadmin.models import User  
from django.shortcuts import render
# from .models import User

def my_view(request):
    return render(request, 'index.html')

def product(request):
    return render(request, 'product.html')

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

def signup(register):
    