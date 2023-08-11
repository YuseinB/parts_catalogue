from django.contrib import admin
from django.urls import path, include
from .web.views import index, WhoAreWe, Contacts
from .search.views import search_parts


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', search_parts, name='index'),
    path('whe_are/', WhoAreWe.as_view(), name='whe_are'),
    path('contacts/', Contacts.as_view(), name='contacts'),
    path('users/', include('parts_catalogue.users.urls')),
    path('web/', include('parts_catalogue.web.urls')),
    path('errors/', include('parts_catalogue.errors.urls')),
]

