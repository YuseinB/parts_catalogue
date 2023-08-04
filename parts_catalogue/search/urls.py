from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_parts, name='search_parts'),
]
