from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.shortcuts import redirect


from .models import product
# from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    sucess_url = reverse_lazy('login')
    template_name = 'signup.html'

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})
        


def HomeView(request):
    context = {
        'products' : product.objects.all()
    }
    return render(request, 'index.html', context)


def product_details(request, product_id):
    products = get_object_or_404(product, pk=product_id)
    return render(request, 'product.html', {'products':products})





