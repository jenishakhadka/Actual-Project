from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    address = models.CharField(max_length=50, default='')
    phone_no = models.CharField(max_length=10, default='')
    is_cust = models.BooleanField(default=True)
    is_delivery = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

class Category(models.Model):
    name = models.CharField(max_length = 40)

    def __str__(self):
        return str(self.name)

class product(models.Model):
     product_name = models.CharField(max_length = 100)
     product_image = models.ImageField(upload_to='product', default='')
     category     = models.ForeignKey(Category, on_delete = models.CASCADE)
     price        = models.IntegerField(default=0)
     quantity     = models.IntegerField(default=0)
     mfg_date     = models.DateTimeField()
     exp_date     = models.DateTimeField()
     dosage       = models.IntegerField()

     def __str__(self):
         return str(self.product_name)
