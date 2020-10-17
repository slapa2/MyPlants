from django.contrib.auth.models import User

from rest_framework import generics, permissions


from .models import Plant
from .serializers import PlantSerializer

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
