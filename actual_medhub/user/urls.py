from django.urls import path
from .views import HomeView, product_details

urlpatterns = [
    path('', HomeView, name='home'),
    path('<int:product_id>/', product_details, name='product'),
]
