from django.contrib.auth.models import User

from rest_framework import generics, permissions
from rest_framework import viewsets

from .models import Plant
from .serializers import PlantSerializer

# PLANTS
class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)