from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ServiceCategoryViewSet, ServiceProviderViewSet, ServiceViewSet, index, service_list, login_view, register_view # Import new views

router = DefaultRouter()
router.register(r'categories', ServiceCategoryViewSet)
router.register(r'providers', ServiceProviderViewSet)
router.register(r'services', ServiceViewSet)

urlpatterns = [
    path('', index, name='index'), # Add this line for the homepage
    path('services/', service_list, name='service_list'), # Add this line for the service list page
    path('login/', login_view, name='login'), # New URL for login
    path('register/', register_view, name='register'), # New URL for register
] + router.urls # Combine with router URLs