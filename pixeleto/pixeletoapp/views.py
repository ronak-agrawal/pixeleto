# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import traceback

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from .serializers import UserSerializer
from .models import User
from rest_framework import status


# get user by id
@csrf_exempt
@api_view(["GET"])
def get_user(request, id):
    user = User.objects.get(id=id)
    serializer = UserSerializer(user)
    return JsonResponse({'user': serializer.data}, safe=False, status=status.HTTP_200_OK)

# get all users
@csrf_exempt
@api_view(["GET"])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    #todo add pagination
    return JsonResponse({'users': serializer.data}, safe=False, status=status.HTTP_200_OK)


# add user
@csrf_exempt
@api_view(["POST"])
def add_user(request):
    payload = request.data
    # payload = json.loads(json.dumps(request.data))
    try:
        user = User.objects.create(
            name=payload["name"],
            age=payload["age"],
            email=payload["email"]
        )
        serializer = UserSerializer(user)
        return JsonResponse({'user': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except:
        traceback.print_exc()
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# edit user by id
@csrf_exempt
@api_view(["PUT"])
def edit_user(request, id):
    payload = json.loads(request.body)
    try:
        user = User.objects.get(id=id)
        # returns 1 or 0
        user.update(**payload)
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return JsonResponse({'user': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# delete user by id
@csrf_exempt
@api_view(["DELETE"])
def delete_user(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return JsonResponse({'message' : 'user deleted successfully'}, safe=False, status=status.HTTP_204_NO_CONTENT)
    except:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)