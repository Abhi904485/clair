from django.urls import path

from .api_views import scan_image_klar

app_name = 'klar_api'
urlpatterns = [
    path(r'', scan_image_klar, name="scan_image"),
]
