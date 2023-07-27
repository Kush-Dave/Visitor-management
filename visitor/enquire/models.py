from django.db import models
from datetime import date, datetime
from django.utils.translation import gettext as _

# Create your models here.

class detail(models.Model):
  name = models.CharField(max_length=50, default=False)
  number = models.IntegerField(default=False)
  email = models.EmailField(max_length=50, default=False)
  company_name = models.CharField(max_length=50,default=False)
  # products = 
  date = models.DateField(_("Date"), default=date.today)