from django.urls import path
from .views import scan_image

app_name = 'klar'
urlpatterns = [
    path('', scan_image, name='scan_image'),
]
