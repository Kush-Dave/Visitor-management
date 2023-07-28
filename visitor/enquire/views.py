from django.shortcuts import render
from .models import detail, product
from datetime import date
# Create your views here.

def index(request):
  return render(request, 'index.html')

def home(request):
  if request.method == 'POST':
    name = request.POST.get['name']
    number = request.POST.get['number']
    email = request.POST.get['email']
    company_name = request.POST.get['company_name']
    product = request.POST.get['product']
    sel_product = detail.objects.filter(project__iexact = product)
    obj = detail.objects.create(name=name, number=number, email=email, product=product, company_name=company_name)
    obj.save()
  return render(request, 'home.html')

def products(request):
  if request.method == 'POST':
    product_name = request.POST.get['product_name']
    
    obj1 = product.objects.create(product_name=product_name)
    obj1.save()
  return render(request, 'products.html')