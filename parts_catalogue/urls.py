from django.contrib import admin
from django.urls import path, include
from .errors.views import handler404
from .web.views import index
from .search import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('search/', include('parts_catalogue.search.urls')),
    path('users/', include('parts_catalogue.users.urls')),
    path('web/', include('parts_catalogue.web.urls')),
    path('errors/', include('parts_catalogue.errors.urls')),
]
handler404 = handler404