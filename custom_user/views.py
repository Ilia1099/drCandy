from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny

from .permissions.custom_user_permissions import IsAdminOrOwner, IsOwner
from .serializers import CustomerSerializer, CustomerProfileSerializer
from .models import CustomerProfile, User


class UsersViewSet(viewsets.ModelViewSet):
    """Viewset which implements CRUD operations for users endpoint"""
    permission_classes = [IsAdminUser]

    lookup_field = 'id'
    serializer_class = CustomerSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        match self.action:
            case "list":
                permission_classes = [IsAdminUser]
            case "create":
                permission_classes = [AllowAny]
            case _:
                print("check other actions")
                permission_classes = [IsAdminOrOwner]
        return [permission() for permission in permission_classes]


class CustomerProfileViewSet(
    viewsets.ModelViewSet
):
    """Viewset which implements CRUD operations for users' profile endpoint - to be implemented"""
    permission_classes = [IsOwner]
    serializer_class = CustomerProfileSerializer
    queryset = CustomerProfile.objects.all()
    lookup_field = 'customer_id_id'

    def get_queryset(self):
        return self.queryset.filter(customer_id_id=self.request.user.id)
