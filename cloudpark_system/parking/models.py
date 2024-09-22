from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    card_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    plate = models.CharField(max_length=10, unique=True)
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.plate

class Plan(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Contract(models.Model):
    name = models.CharField(max_length=255)
    max_value = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_minute = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class ParkMovement(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)
    contract = models.ForeignKey(Contract, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.vehicle} - {self.entry_time}'