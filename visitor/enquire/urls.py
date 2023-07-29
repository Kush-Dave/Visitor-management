from django.urls import path
from . import views
# from django.conf.urls import url
from wkhtmltopdf.views import PDFTemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('products', views.prod, name='products'),
    # url(r'^pdf/$', PDFTemplateView.as_view(template_name='my_template.html',
    #                                        filename='my_pdf.pdf'), name='pdf'),
]