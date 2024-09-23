from rest_framework import serializers
from .models import Customer, Vehicle, Plan, CustomerPlan, Contract, ContractRule, ParkMovement

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

class CustomerPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPlan
        fields = '__all__'

class ContractRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractRule
        fields = ['until', 'value']

class ContractSerializer(serializers.ModelSerializer):
    rules = ContractRuleSerializer(many=True, required=False)

    class Meta:
        model = Contract
        fields = ['id', 'description', 'max_value', 'rules']

    def create(self, validated_data):
        rules_data = validated_data.pop('rules', [])
        contract = Contract.objects.create(**validated_data)
        for rule in rules_data:
            ContractRule.objects.create(contract=contract, **rule)
        return contract
    
    def update(self, instance, validated_data):
        rules_data = validated_data.pop('rules', [])
        instance = super().update(instance, validated_data)
    
        instance.rules.all().delete()
        for rule_data in rules_data:
            ContractRule.objects.create(contract=instance, **rule_data)
        return instance

class ParkMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkMovement
        fields = '__all__'
