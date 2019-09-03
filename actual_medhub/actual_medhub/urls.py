from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from user.views import SignUpView, signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('signup/', signup, name='signup'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
