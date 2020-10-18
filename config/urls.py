"""myplants URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from django.contrib import admin
from apps.plants import views as plant_views

router = DefaultRouter()
router.register(r'api/plants', plant_views.PlantViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',  include(router.urls)),

    path('api/userplant/',      include('apps.users_plants.urls')),
    path('api-auth/',           include('rest_framework.urls')),
    path('api/auth/',           include('apps.users.urls')),

]
