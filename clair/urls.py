"""clair URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import home

admin.site.site_header = "Container Security Admin Portal "
admin.site.site_title = "CVS Admin Portal"
admin.site.index_title = "Welcome to CVS Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', home, name='home'),
    path('klar/', include('klar.urls', namespace='klar')),
    path('klar_api/', include('klar.api_urls', namespace='klar_api')),
    path('raw_query/',include('raw_query.urls',namespace='raw_query')),
    path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
