from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    is_cust = models.BooleanField(default=True)
    is_delivery = models.BooleanField(default=False)

class Category(models.Model):
    name = models.CharField(max_length = 40)

class product(models.Model):
     product_name = models.CharField(max_length = 100)
     category     = models.ForeignKey(Category, on_delete = models.CASCADE)
     price        = models.IntegerField()
     mfg_date     = models.DateTimeField()
     exp_date     = models.DateTimeField()
     dosage       = models.IntegerField()
