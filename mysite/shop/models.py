from django.db import models

# Create your models here.
# Django Field Reference.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    pub_Date=models.DateField()