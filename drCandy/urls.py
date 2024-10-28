from django.contrib import admin
from django.urls import path, include
from api.v1.router import urlpatterns as api_urls
from api_auth.views import SessionLogin
from .views import MainPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('admin/', admin.site.urls, name='admin'),
    path(f'api/v1/', include(api_urls), name='api_v1'),
    path(f'auth/', SessionLogin.as_view(), name='auth'),
]


# TODO
# Create viewsets for all endpoints
