from django.shortcuts import render
from .models import detail
from datetime import date
# Create your views here.

def index(request):
  return render(request, 'index.html')

def home(request):
  if request.method == 'POST':
    name = request.POST['name']
    number = request.POST['number']
    email = request.POST['email']
    company_name = request.POST['company_name']
    
    eve = detail.objects.create(name=name,number=number,email=email,company_name=company_name,date=date)
    eve.save()
  return render(request, 'home.html')