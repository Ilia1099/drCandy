from django.contrib import admin
from django.urls import path, include
from api.v1 import router as rv1
from .views import MainPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('admin/', admin.site.urls, name='admin'),
    path(f'api/v1/', include(rv1.urls), name='api_v1'),
]


# TODO
# Implement def create() methods for serializers
# Create viewsets for all endpoints
