from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'Catalog/index.html')

def about(request):
    return render(request, 'Catalog/about.html')

def products(request):
    return render(request, 'Catalog/products.html')

def contact(request):
    return render(request, 'Catalog/contact.html')