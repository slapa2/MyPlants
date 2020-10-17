
from django.urls import path

from . import views

urlpatterns = [
    path('', views.PlantList.as_view()),
    path('<int:pk>', views.PlantDetail.as_view(), name='plant-detail'),

    path('userplant', views.UserPlantList.as_view()),
    path('userplant/<int:pk>', views.UserPlantDetails.as_view()),
    path('userplant/event/create', views.PlantEventCreate.as_view()),
    path('userplant/event/<int:pk>', views.PlantEventDetails.as_view()),
]
