from django.urls import path, include
from rest_framework.routers import DefaultRouter
from parking.views import ContractViewSet, CustomerViewSet, ParkMovementViewSet, PlanViewSet, VehicleViewSet

router = DefaultRouter()
router.register(r'customer', CustomerViewSet)
router.register(r'vehicle', VehicleViewSet)
router.register(r'plan', PlanViewSet)
router.register(r'contract', ContractViewSet)
router.register(r'parkmovement', ParkMovementViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]