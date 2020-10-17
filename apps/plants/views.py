from django.contrib.auth.models import User

from rest_framework import generics, permissions
from rest_framework.parsers import JSONParser


from .models import Plant, UserPlant, PlantEvent
from .serializers import PlantSerializer, UserPlantSerializer, PlantEventSerializer

# PLANTS
class PlantList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


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