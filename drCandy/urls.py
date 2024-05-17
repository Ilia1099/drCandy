from django.contrib import admin
from django.urls import path, include
from api.router import router as rt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(rt.urls)),
]


# TODO
# Implement def create() methods for serializers
# Create viewsets for all endpoints
