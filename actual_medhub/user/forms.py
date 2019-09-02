from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserDetails

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = UserDetails
        fields = ('age', 'is_cust', 'is_delivery')

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = UserDetails
        fields = ('age', 'is_cust', 'is_delivery')