from rest_framework import serializers
from .models import ServiceCategory, ServiceProvider, Service
from users.models import CustomUser # Assuming CustomUser is in users.models

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name'] # Add other fields as needed

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = '__all__'

class ServiceProviderSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True) # Nested serializer for user details
    services = serializers.PrimaryKeyRelatedField(queryset=ServiceCategory.objects.all(), many=True)

    class Meta:
        model = ServiceProvider
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    provider = serializers.PrimaryKeyRelatedField(queryset=ServiceProvider.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=ServiceCategory.objects.all())

    class Meta:
        model = Service
        fields = '__all__'