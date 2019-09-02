from django.urls import path
from .views import homepage, SignUpView

urlpatterns = [
    path('', homepage, name='home'),
    path('signup/', SignUpView.as_view(), name = 'signup')
]
