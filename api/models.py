from django.db import models
from dateutil.relativedelta import *
from dateutil.parser import *
from datetime import *

# Create your models here.
class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=datetime.now().date())
    customerName = models.CharField(max_length=50)

class InvoiceDetail(models.Model):
    id = models.AutoField(primary_key=True)
    invoiceID = models.ForeignKey(Invoice, on_delete=models.CASCADE, db_column='invoiceID')
    description = models.CharField(max_length=300)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    price = models.IntegerField()