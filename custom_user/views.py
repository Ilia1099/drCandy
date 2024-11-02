from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .serializers import CustomerSerializer, CustomerProfileSerializer
from .models import CustomerProfile, User


class UsersViewSet(viewsets.ModelViewSet):
    """Viewset which implements CRUD operations for users endpoint"""
    permission_classes = [IsAdminUser]

    lookup_field = 'id'
    serializer_class = CustomerSerializer
    queryset = User.objects.all()


class CustomerProfileViewSet(viewsets.ModelViewSet):
    """Viewset which implements CRUD operations for users' profile endpoint - to be implemented"""
    ...
