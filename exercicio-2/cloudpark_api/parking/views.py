from rest_framework import viewsets

from parking.models import Contract, Customer, ParkMovement, Plan, Vehicle
from parking.serializers import ContractSerializer, CustomerSerializer, ParkMovementSerializer, PlanSerializer, VehicleSerializer

# Create your views here.

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class ParkMovementViewSet(viewsets.ModelViewSet):
    queryset = ParkMovement.objects.all()
    serializer_class = ParkMovementSerializer
    
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer