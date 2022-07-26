from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from user_app.models import UserCredential
from user_app.serializers import UserSerializer, UserCredentialSerializer
from mood_app.models import Content
from .models import *
from .serializers import *


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


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_user_fav(request: Request, content_id):
    '''
    this function add new liked content into loged user favorite table
    '''
    if request.user.is_authenticated:
        loged_user = User.objects.get(id=request.user.id)
        new_contant = Content.objects.get(id=content_id)
        fav_contant = Favorite.objects.create(user=loged_user, Content=new_contant)

        dataResponse = {
            'msg': 'Success',
            'new_contant': f'{fav_contant.Content.mood.name}' }


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def get_user_fav(request : Request):
    """
     this API to get loged user fav
     """

    if request.user.is_authenticated:
        loged_user = User.objects.get(id=request.user.id)
        user_fav = Favorite.objects.filter(user=loged_user)

        dataResponse = {
            'msg': f'user {request.user.username} fav',
            'fav': FavoriteSerializer(instance=user_fav ,many=True).data
        }

        return Response(dataResponse, status=status.HTTP_200_OK)

    else:
        dataResponse = {'msg': 'unathurazed access'}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_rating(request: Request):
    '''
     this function add new user rating into ratting table
    :param request:
    :return:dataResponse
    '''
    if request.user.is_authenticated:
        loged_user = User.objects.get(id=request.user.id)
        new_rating = Rating.objects.create(user=loged_user, rating=request.data['rating'])

        dataResponse = {
            'msg': f'user {request.user.username} posted rating',
            'fav': RatingSerializer(instance=new_rating).data
        }

        return Response(dataResponse, status=status.HTTP_200_OK)

    else:
        dataResponse = {'msg': 'unathurazed access'}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_overall_rating_AVG(request: Request):
    '''
    this function calc the overall rating of the website
    :param request:
    :return:
    '''
    ratings = Rating.objects.all()
    avg = sum([i.rating for i in ratings])/Rating.objects.count()

    dataResponse = {
        'msg': f'overall rating of the website',
        'AVG': f'{avg}'
    }
    return Response(dataResponse, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def get_user_rating_avg(request: Request):
    '''
     this function calc loged user rating avg
    :param request:
    :return:dataResponse
    '''
    if request.user.is_authenticated:
     loged_user = User.objects.get(id=request.user.id)
     ratings = Rating.objects.filter(user=loged_user)
     avg = sum([i.rating for i in ratings]) / ratings.count()

     dataResponse = {
        'msg': f'user {request.user.username} avg rating of the website',
        'AVG': f'{avg}'
     }
     return Response(dataResponse, status=status.HTTP_200_OK)

