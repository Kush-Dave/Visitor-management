from django.shortcuts import render, HttpResponse
from django.http import FileResponse
import reportlab
import io
from reportlab.pdfgen import canvas
from django.views import View
from .models import detail
from datetime import date
from django.contrib import messages
# Create your views here.

def index(request):
  return render(request, 'index.html')

def home(request):
  if request.method == 'POST':
    name = request.POST['name']
    number = request.POST['number']
    email = request.POST['email']
    company_name = request.POST['company_name']
    product_name = request.POST['product_name']
  #   selected_value = request.POST.get['selected_product']
  #   product_search = detail.objects.values_list('project',flat=True).distinct()
  #   sel_product = detail.objects.filter(prodct_name__iexact = selected_value)
    
  # context = {
  #   'selected_value' : selected_value,
  #   'product_search':product_search,
  #   'sel_product': sel_product,      
  # }
    obj = detail.objects.create(name=name, number=number, email=email, product_name=product_name, company_name=company_name)
  
    obj.save()
    messages.error(request, "Form Submitted successfully")
  return render(request,'home.html')

def prod(request):
  if request.method=="POST":
    fromdate = request.POST['fromdate']
    todate = request.POST['todate']
    search_list = detail.objects.all()
    return render(request, 'products.html',{'obj1':search_list})
  else:
    obj1 = detail.objects.all()
    return render(request, 'products.html',{'obj1':obj1})
  
# class ViewPDF(View):
#   def get(self, request, *args, **kwargs):
#       context={}
#       context['user'] =detail.objects.all()
#       pdf = render_to_pdf('product.html',context_dict=context)
#       return HttpResponse(pdf, content_type='application/pdf')

# def some_view(request):
#     # Create a file-like buffer to receive PDF data.
#     buffer = io.BytesIO()

#     # Create the PDF object, using the buffer as its "file."
#     p = canvas.Canvas(buffer)

#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.
#     p.drawString(100, 100, "Hello world.")

#     # Close the PDF object cleanly, and we're done.
#     p.showPage()
#     p.save()

#     # FileResponse sets the Content-Disposition header so that browsers
#     # present the option to save the file.
#     buffer.seek(0)
#     return FileResponse(buffer, as_attachment=True, filename="hello.pdf")