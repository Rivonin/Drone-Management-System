from django.db import models

class Drone(models.Model):
    MODELS = [
        ('LW', 'Lightweight'),
        ('MW', 'Middleweight'),
        ('CW', 'Cruiserweight'),
        ('HW', 'Heavyweight'),
    ]
    STATES = [
        ('IDLE', 'Idle'),
        ('LOADING', 'Loading'),
        ('LOADED', 'Loaded'),
        ('DELIVERING', 'Delivering'),
        ('DELIVERED', 'Delivered'),
        ('RETURNING', 'Returning'),
    ]
    serial_number = models.CharField(max_length=100, unique=True)
    model = models.CharField(max_length=2, choices=MODELS)
    weight_limit = models.DecimalField(max_digits=5, decimal_places=2)
    battery_capacity = models.PositiveIntegerField()
    state = models.CharField(max_length=15, choices=STATES)

class Medication(models.Model):
    name = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    code = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='medications/')

# drones/serializers.py
from rest_framework import serializers
from .models import Drone, Medication

class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = '__all__'

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'