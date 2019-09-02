from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


from .models import UserDetails
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    sucess_url = reverse_lazy('login')
    template_name = 'signup.html'


def homepage(request):
    if request.user.is_authenticated:
        return HttpResponse("<h1>You are authincated!</h1>")
    return render(request, 'home.html')

