
from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserPlantList.as_view()),
    path('<int:pk>', views.UserPlantDetails.as_view()),
    path('event/create', views.PlantEventCreate.as_view()),
    path('event/<int:pk>', views.PlantEventDetails.as_view()),
]
