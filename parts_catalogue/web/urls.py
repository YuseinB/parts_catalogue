from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addpart/', views.add_part, name='add_part'),
    path('addcat/', views.add_category, name='add_category'),
]
