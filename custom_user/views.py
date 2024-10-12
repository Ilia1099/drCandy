from rest_framework import viewsets
from rest_framework.generics import mixins
from .serializers import CustomerSerializer, CustomerProfileSerializer
from .models import CustomerProfile, User


class UsersViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    lookup_field = 'id'
    serializer_class = CustomerSerializer
    queryset = User.objects.all()

