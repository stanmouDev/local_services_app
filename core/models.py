from django.db import models
from django.conf import settings

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class ServiceProvider(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='provider_pics/', blank=True, null=True) # New field
    services = models.ManyToManyField('ServiceCategory', related_name='providers')

    def __str__(self):
        return self.user.username

class Service(models.Model):
    provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE, related_name='offered_services')
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services_in_category')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.name} by {self.provider.user.username}"