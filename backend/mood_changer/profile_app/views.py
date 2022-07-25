
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from user_app.models import UserCredential
from .serializers import *
from user_app.serializers import UserSerializer, UserCredentialSerializer
from .models import *


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def get_user_info(request : Request):
    """
    this API to get loged user info
    """

    if request.user.is_authenticated:
        loged_user = User.objects.get(id= request.user.id)
        user_crudintal = UserCredential.objects.get(user=loged_user)
        dataResponse ={
            'msg': f'user {request.user.username} info',
            'info': UserSerializer(instance=loged_user).data,
            'pic': UserCredentialSerializer(instance=user_crudintal).data
        }
        return Response(dataResponse, status=status.HTTP_200_OK)
    else:
        dataResponse = {'msg':  'unathurazed access'}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)