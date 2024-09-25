from django.forms import ValidationError
from rest_framework import viewsets, status
from rest_framework.response import Response
from parking.models import Contract, Customer, ParkMovement, Plan, Vehicle
from parking.serializers import ContractSerializer, CustomerSerializer, ParkMovementSerializer, PlanSerializer, VehicleSerializer

# Create your views here.

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def create(self, request, *args, **kwargs):
       plate = request.data.get('plate')
       has_vehicle = Vehicle.objects.filter(plate=plate).first()

       if (has_vehicle):

          if has_vehicle.customer_id: 
             return Response({"error": "Veículo já está vinculado a um cliente."}, status=status.HTTP_400_BAD_REQUEST)
          else:  
             return Response({"info": "O veículo já está cadastrado como rotativo. Link a um cliente se necessário!."})
       return super().create(request, *args, **kwargs)
      
class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
        
class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

class ParkMovementViewSet(viewsets.ModelViewSet):
    queryset = ParkMovement.objects.all()
    serializer_class = ParkMovementSerializer
    
    def perform_create(self, serializer):
        vehicle = serializer.validated_data.get('vehicle_id')
        
        if not vehicle.plate:
            raise ValidationError("Veículo deve ter uma placa válida.")
        
        vehicle.in_parking = True
        vehicle.save()
        
        serializer.save() 
    
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer