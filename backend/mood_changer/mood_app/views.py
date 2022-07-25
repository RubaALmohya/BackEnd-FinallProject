from .serializers import *
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes

from django.contrib.auth.models import User
from user_app.models import UserCredential,UserMood

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def user_moods(request : Request):
    '''
    this method list all the previous users moods state.
    :param: request
    :return: dataResponse
    '''

    # get list of moods id
    try:
      loged_user = User.objects.get(id = request.user.id)
      user_moods = UserMood.objects.filter(user=loged_user) #UserMoods attribute(id, user, mood, date)

      user_moods_info = {str(i.date)[:10] : Mood.objects.get(id = i.mood.id) for i in user_moods }


      dataResponse = {
        "msg" : f"List of All user {request.user.username} moods",
        "user_moods" : f'{user_moods_info}'
      }
      return Response(dataResponse, status=status.HTTP_200_OK)
    except Exception as e:
     return Response(f'{e}', status=status.HTTP_400_BAD_REQUEST)


