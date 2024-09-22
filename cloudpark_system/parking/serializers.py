from rest_framework import serializers
from .models import Customer, Vehicle, Plan, Contract, ParkMovement

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

class ParkMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkMovement
        fields = '__all__'