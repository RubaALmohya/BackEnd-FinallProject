from .serializers import *
from rest_framework import status
from rest_framework.request import Request
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import AccessToken


@api_view(['POST'])
def register(request: Request):
    '''
    A register method for user
    '''
    User_serializer = UserSerializer(data=request.data)

    if User_serializer.is_valid():
        User_serializer.save()
        return Response({"msg": "New user hase been created"})
    else:
        print(User_serializer.errors)
        return Response({"msg": "Couldn't create a user"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request: Request):
    '''
    A method for login
    '''
    if 'username' in request.data and 'password' in request.data:
      try:
        user = User.objects.get(username=request.data['username'], password=request.data['password'])

        token = AccessToken.for_user(user)
        dataResponse = {
                "msg": "Your token have been generated",
                "token": str(token)
            }
        return Response(dataResponse)
      except Exception:
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token = AccessToken.for_user(user)
            dataResponse = {
                "msg": "Your token have been generated",
                "token": str(token)
            }
            return Response(dataResponse)

    return Response({"msg": "please provide your username & password"}, status=status.HTTP_401_UNAUTHORIZED)


