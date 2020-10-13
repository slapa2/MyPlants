from typing import Type
from django.db.utils import Error
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.db import IntegrityError

from rest_framework.parsers import JSONParser

@csrf_exempt
def sign_up(request):
    """
    curl -X POST http://127.0.0.1:8000/api/auth/signup -H 'Content-Type": application/json' -d '{"username":"someusername","password":"somepassword"}'
    """

    if request.method == "POST":
        # todo password validation
        try:
            data =JSONParser().parse(request)
            user = User.objects.create_user(data.get('username'), password = data.get('password'))
            return JsonResponse({'signed_up': True}, status = 201)
        except IntegrityError:
            return JsonResponse({'error': "Can not create user, this username is already taken"}, status = 400)
        except ValueError:
            return  JsonResponse({'error': "Can not create user, please enter username and password"}, status = 400)

@csrf_exempt
def sign_in(request):
    """
    curl -X POST http://127.0.0.1:8000/api/auth/signin -H 'Content-Type: application/json' -d '{"username":"admin","password":"admin"}'
    """

    if request.method == "POST":
        data =JSONParser().parse(request)
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if user is not None:
            login(request, user=user)
            return JsonResponse({'loged_in': True}, status = 200)
        else:
            return JsonResponse({'error': "Can not login, check your username and password"}, status = 400)

@csrf_exempt
def sign_out(request):
    """
    curl -X POST http://127.0.0.1:8000/api/auth/signout
    """

    if request.method == "POST":
        logout(request)
        return JsonResponse({'loged_out': True}, status = 200)