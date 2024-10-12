from rest_framework import viewsets
from rest_framework.generics import mixins, get_object_or_404
from rest_framework.response import Response

from .serializers import CustomerSerializer, CustomerProfileSerializer
from .models import CustomerProfile, User


class UsersViewSet(viewsets.ModelViewSet):

    lookup_field = 'id'
    serializer_class = CustomerSerializer
    queryset = User.objects.all()

