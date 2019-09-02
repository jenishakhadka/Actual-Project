from django.contrib import admin
from .models import UserDetails, Category, product


admin.site.register(UserDetails)
admin.site.register(Category)
admin.site.register(product)
