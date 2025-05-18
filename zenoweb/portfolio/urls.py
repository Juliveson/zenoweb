from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('submit-service-form/', views.service, name='service') 
]

# Adding static and media URL configurations
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)