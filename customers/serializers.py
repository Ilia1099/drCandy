from rest_framework import serializers
from .models import Customers, CustomerProfile


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['id', 'mobile_number', 'email', 'is_active', 'date_created', 'date_updated']
        read_only_fields = ['id', 'is_active', 'date_created', 'date_updated']


class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = ['customer_id', 'first_name', 'last_name', 'profile_img', 'date_of_birth', 'date_created',
                  'date_updated']
        read_only_fields = ['customer_id', 'date_created', 'date_updated', 'profile_img',]



