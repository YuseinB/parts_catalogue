from django.contrib import admin
from django.urls import path, include
from .errors.views import handler404
from .web.views import index
from .search.views import search_parts


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', search_parts, name='index'),
    path('users/', include('parts_catalogue.users.urls')),
    path('web/', include('parts_catalogue.web.urls')),
    path('errors/', include('parts_catalogue.errors.urls')),
]
handler404 = handler404