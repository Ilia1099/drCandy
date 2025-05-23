from rest_framework import serializers
from .models import User, CustomerProfile


class CustomerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        instance = User.objects.create_user(**validated_data)
        return instance

    class Meta:
        model = User
        fields = ['id', 'mobile_number', 'password', 'email', 'first_name', 'last_name', 'username', 'is_customer']
        read_only_fields = ['id', 'is_active', 'date_joined']
        extra_kwargs = {
            "password": {"write_only": True, "required": True},
            "email": {"required": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
            "username": {"required": True},
            "is_customer": {"required": True}
        }


class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = ['customer_id', 'profile_img', 'date_of_birth', 'date_created',
                  'date_updated']
        read_only_fields = ['date_created', 'date_updated']



