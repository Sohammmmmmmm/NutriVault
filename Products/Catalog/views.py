from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import redirect
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'Catalog/index.html')

def about(request):
    return render(request, 'Catalog/about.html')

def products(request):
    return render(request, 'Catalog/products.html')

def contact(request):
    return render(request, 'Catalog/contact.html')

def Login(request):
    Name = ""
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Password = request.POST.get('Password')
        if not Customer.objects.filter(Name=Name).exists():
            messages.error(request, "Invalid Username")
        elif not Customer.objects.filter(Name=Name, Password=Password).exists():
            messages.error(request, "Invalid Password")
        else:
            messages.success(request,f"Welcome {Name}!")
            return redirect('index')
    return render(request, 'Catalog/Login.html')

def SignUp(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        if Customer.objects.filter(Name=Name).exists():
            messages.error(request, "Account already exists")
        else:
            customer = Customer(Name=Name,Email=Email,Password=Password)
            customer.save()
            messages.success(request, f"Account created successfully for {Name}! You can now log in.")
            return redirect('Login')
            
    return render(request, 'Catalog/SignUp.html')