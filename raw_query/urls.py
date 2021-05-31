from django.urls import path
from .views import raw_query

app_name = "raw_query"
urlpatterns = [
    path('', raw_query, name="raw_query")
]
