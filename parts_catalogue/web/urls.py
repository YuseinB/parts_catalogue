from django.urls import path, include
from . import views
from .views import PartDetailView

urlpatterns = [
    path('search/', include('parts_catalogue.search.urls')),
    path('addpart/', views.add_part, name='add_part'),
    path('part_detail/<int:pk>/', PartDetailView.as_view(), name='part_detail'),
    path('part_detail/edit/<int:pk>/', views.edit_part, name='edit_part'),
    path('addcat/', views.add_category, name='add_category'),
]
