from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


from .models import UserDetails, product
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    sucess_url = reverse_lazy('login')
    template_name = 'signup.html'


def HomeView(request):
    context = {
        'products' : product.objects.all()
    }
    return render(request, 'index.html', context)





