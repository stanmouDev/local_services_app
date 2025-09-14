from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets
from .models import ServiceCategory, ServiceProvider, Service
from .serializers import ServiceCategorySerializer, ServiceProviderSerializer, ServiceSerializer

# Function-based view for the homepage
def index(request):
    return render(request, 'core/index.html')

# Function-based view for listing services
def service_list(request):
    services = Service.objects.all()
    query = request.GET.get('q') # Get the search query from GET parameters

    if query:
        services = services.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query) |
            Q(provider__user__username__icontains=query)
        ).distinct() # Use distinct to avoid duplicate results if a service matches multiple criteria

    context = {'services': services, 'query': query} # Pass query back to template
    return render(request, 'core/service_list.html', context)

# Placeholder view for login
def login_view(request):
    return render(request, 'core/login.html')

# Placeholder view for registration
def register_view(request):
    return render(request, 'core/register.html')

class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer

class ServiceProviderViewSet(viewsets.ModelViewSet):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer