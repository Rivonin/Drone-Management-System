from celery import shared_task
from .models import Drone

@shared_task
def check_battery_levels():
    drones = Drone.objects.all()
    for drone in drones:
        print(f"Drone {drone.serial_number} battery level: {drone.battery_capacity}%")