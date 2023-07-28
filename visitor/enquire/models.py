from django.db import models
from datetime import date, datetime
from django.utils.translation import gettext as _

# Create your models here.

class detail(models.Model):
  name = models.CharField(max_length=50, default=False)
  number = models.IntegerField(default=False)
  email = models.EmailField(max_length=50, default=False)
  company_name = models.CharField(max_length=50,default=False)
  products_choice = (
      ('I1','Item 1'),
      ('I2','Item 2'),
      ('I3','Item 3'),
      ('I4','Item 4'),
      ('I5','Item 5'),
    )
  product = models.CharField(choices=products_choice, max_length=5, default=False)
  date = models.DateField(_("Date"), default=date.today)
  
  

class product(models.Model):
  product_name = models.CharField(max_length=50, default=False)