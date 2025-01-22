from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Drone, Medication
from .serializers import DroneSerializer, MedicationSerializer
from django.http import HttpResponse

def drone(request):
    return HttpResponse("Welcome to the Drone Management System!")



class RegisterDroneAPIView(APIView):
    def post(self, request):
        serializer = DroneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoadMedicationAPIView(APIView):
    def post(self, request, drone_id):
        try:
            drone = Drone.objects.get(id=drone_id)
        except Drone.DoesNotExist:
            return Response({"error": "Drone not found."}, status=status.HTTP_404_NOT_FOUND)

        if drone.state != 'LOADING' or drone.battery_capacity < 25:
            return Response({"error": "Drone cannot be loaded."}, status=status.HTTP_400_BAD_REQUEST)

        medications = request.data.get('medications', [])
        total_weight = sum([Medication.objects.get(id=med_id).weight for med_id in medications])

        if total_weight > drone.weight_limit:
            return Response({"error": "Exceeds weight limit."}, status=status.HTTP_400_BAD_REQUEST)

        drone.state = 'LOADED'
        drone.save()
        return Response({"message": "Drone loaded successfully."}, status=status.HTTP_200_OK)
