from django.utils import timezone
from django.db import models

# Create your models here.

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    card_id = models.CharField(max_length=50, unique=True)

class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    plate = models.CharField(max_length=10, unique=True)
    model = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=255, default='')
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255, default='')
    value = models.FloatField()
    
class CustomerPlan(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    plan_id = models.ForeignKey(Plan, on_delete=models.CASCADE)
    due_date = models.DateTimeField(default=timezone.now)  

class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255, default='')
    max_value = models.FloatField(null=True)

class ContractRule(models.Model):
    id = models.AutoField(primary_key=True)
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE, )
    until = models.IntegerField()
    value = models.FloatField()
    
class ParkMovement(models.Model):
    id = models.AutoField(primary_key=True)
    entry_date = models.DateTimeField(default=timezone.now) 
    exit_date = models.DateTimeField(default=timezone.now)  
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    value = models.FloatField(null=True)

    def __str__(self):
        return f'{self.vehicle} - {self.entry_time}'