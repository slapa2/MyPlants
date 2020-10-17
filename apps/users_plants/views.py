from rest_framework import generics, permissions

from .models import UserPlant, PlantEvent
from .serializers import UserPlantSerializer, PlantEventSerializer

# USER-PLANTS
class UserPlantList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserPlantSerializer

    def get_queryset(self):
        return UserPlant.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserPlantDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserPlantSerializer

    def get_queryset(self):
        return UserPlant.objects.filter(owner=self.request.user)


# PLANTS-EVENTS
class PlantEventCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PlantEventSerializer

    def perform_create(self, serializer):
        user = self.request.user
        user_plant_owner = UserPlant.objects.get(pk=serializer.validated_data.get('user_plant_id')).owner

        #TODO: poprawić walidację i error message
        if user != user_plant_owner:
            raise Exception
        serializer.save()


class PlantEventDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PlantEventSerializer

    def get_queryset(self):
        user_plants = UserPlant.objects.filter(owner=self.request.user)
        return PlantEvent.objects.filter(user_plant__in=user_plants)