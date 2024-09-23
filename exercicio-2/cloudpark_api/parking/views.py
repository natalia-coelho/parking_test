from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import (Customer, Vehicle, Plan, CustomerPlan, Contract, ContractRule, ParkMovement)
from .serializers import (
    CustomerSerializer,
    VehicleSerializer,
    PlanSerializer,
    CustomerPlanSerializer,
    ContractSerializer,
    ContractRuleSerializer,
    ParkMovementSerializer,
)
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

# Create your views here.

class CustomerAPIView(APIView):
   def get(self, request, pk=None):
      serializer = None
      if pk is not None:
         customer = get_object_or_404(Customer, pk=pk)
         serializer = CustomerSerializer(customer)
      else:
         customers = Customer.objects.all()
         serializer = CustomerSerializer(customers, many=True)
      return Response(serializer.data)
   
   def post(self, request):
      serializer = CustomerSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   def put(self, request, pk):
      customer = get_object_or_404(Customer, pk=pk)
      serializer = CustomerSerializer(customer, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VehicleAPIView(APIView):
   def get(self, request, pk=None):
      serializer = None
      if pk is not None:
         vehicle = get_object_or_404(Vehicle, pk=pk)
         serializer = VehicleSerializer(vehicle)
      else:
         vehicles = Vehicle.objects.all()
         serializer = VehicleSerializer(vehicles, many=True)
      return Response(serializer.data)
   
   def post(self, request):
      serializer = VehicleSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   def put(self, request, pk):
      vehicle = get_object_or_404(Vehicle, pk=pk)
      serializer = VehicleSerializer(vehicle, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlanAPIView(APIView):
   def get(self, request, pk=None):
      serializer = None
      if pk is not None:
         plan = get_object_or_404(Plan, pk=pk)
         serializer = PlanSerializer(plan)
      else:
         plan = Plan.objects.all()
         serializer = PlanSerializer(plan, many=True)
      return Response(serializer.data)
   
   def post(self, request):
      serializer = PlanSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   def put(self, request, pk):
      plan = get_object_or_404(Plan, pk=pk)
      serializer = PlanSerializer(plan, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContractAPIView(APIView):
   def get(self, request):
      contract = Contract.objects.all()
      serializer = ContractSerializer(contract, many=True)
      return Response(serializer.data)
   
   def post(self, request):
      serializer = ContractSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   def put(self, request):
      contract = get_object_or_404(Contract, description=request.data.get('description'))
      serializer = ContractSerializer(contract, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerPlanAPIView(APIView):
   def get(self, request, pk=None):
      serializer = None
      if pk is not None:
         customer_plan = get_object_or_404(CustomerPlan, pk=pk)
         serializer = CustomerPlanSerializer(customer_plan)
      else:
         customer_plan = CustomerPlan.objects.all()
         serializer = CustomerPlanSerializer(customer_plan, many=True)
      return Response(serializer.data)
   
   def post(self, request):
      serializer = CustomerPlanSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   def put(self, request, pk):
      customer_plan = get_object_or_404(CustomerPlan, pk=pk)
      serializer = CustomerPlanSerializer(customer_plan, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ParkMovementAPIView(APIView):
   def get(self, request, pk=None):
      serializer = None
      if pk is not None:
         park_moviment = get_object_or_404(ParkMovement, pk=pk)
         serializer = ParkMovementSerializer(park_moviment)
      else:
         park_moviment = ParkMovement.objects.all()
         serializer = ParkMovementSerializer(park_moviment, many=True)
      return Response(serializer.data)
   
   def post(self, request):
      serializer = ParkMovementSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   def put(self, request, pk):
      park_moviment = get_object_or_404(ParkMovement, pk=pk)
      serializer = ParkMovementSerializer(park_moviment, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)