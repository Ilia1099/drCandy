from django.contrib import admin
from django.urls import path, include
from api.v1.router import urlpatterns as api_urls
from .views import MainPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('admin/', admin.site.urls, name='admin'),
    path(f'api/v1/', include(api_urls), name='api_v1'),
]


# TODO
# Create viewsets for all endpoints
