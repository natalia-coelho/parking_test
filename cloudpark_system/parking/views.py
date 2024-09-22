from rest_framework import viewsets
from parking.models import Customer, Vehicle, Plan, Contract, ParkMovement
from .serializers import CustomerSerializer, VehicleSerializer, PlanSerializer, ContractSerializer, ParkMovementSerializer

# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

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