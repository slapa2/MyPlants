from rest_framework import generics, permissions
from rest_framework.parsers import JSONParser


from .models import Plant, UserPlant
from .serializers import PlantSerializer, UserPlantSerializer


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

