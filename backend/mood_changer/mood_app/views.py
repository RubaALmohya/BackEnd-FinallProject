import random

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.decorators import api_view
import joblib
import cv2
from deepface import DeepFace
from django.http import FileResponse
from django.contrib.auth.models import User
from user_app.models import UserCredential,UserMood
from .serializers import *
from .models import *

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def user_moods(request : Request):
    '''
    this method list all the previous user's moods state.
    :param: request
    :return: dataResponse
    '''

    # get list of moods id
    try:
      loged_user = User.objects.get(id = request.user.id)
      user_moods = UserMood.objects.filter(user=loged_user) #UserMoods attribute(id, user, mood, date)

      user_moods_date = [str(i.date)[:10] for i in user_moods]
      user_moods_name = [ i.mood.name for i in user_moods ]
      user_moods_color = [ i.mood.color for i in user_moods ]


      dataResponse = {
        "msg" : f"List of All user {request.user.username} moods",
        "user_moods_date": user_moods_date ,
        "emotion_name" : user_moods_name,
        "emotion_color" : user_moods_color
      }
      return Response(dataResponse, status=status.HTTP_200_OK)
    except Exception as e:
     return Response(f'{e}', status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def TakePhoto(response):
    '''
    This API is to take the picture from the camera
    :param: request
    :return:
    '''
    global photo
    camera = cv2.VideoCapture(0)
    for i in range(1):
        return_value, image = camera.read()
        cv2.imwrite('mood' + str(i) + '.png', image)
        photo = cv2.imread('mood0.png')
        # plt.imshow(cv2.cvtColor(photo, cv2.COLOR_BGR2RGB))
    del (camera)
    img = open('mood0.png', 'rb')
    response = FileResponse(img)
    return response



@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def EmotionPrediction(request: Request):
    '''
    This is an API for classifying and identifying emotion from the captured image using machine learning
    :param: request
    :return:
    '''
    if request.user.is_authenticated:
        predictionImg = DeepFace.analyze('mood0.png')
        ID = request.user.id
        print(predictionImg)
        print(predictionImg['dominant_emotion'])
        filename = 'takephoto.pkl'
        joblib.dump(predictionImg, filename)
        PickleFile=joblib.load("takephoto.pkl")
        userslist = {"msg": "Image Emotion",
                         "details":PickleFile}
        add_userMood( ID,PickleFile)
        return Response(userslist)
    else:
        dataResponse = {'msg': 'unathurazed access'}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def display_content(request: Request):
    '''
    this function displays  the content for the user after emotion analysis by their img
    :param request: Request
    :return:dataResponse
    '''
    if request.user.is_authenticated:
        loged_user = User.objects.get(id=request.user.id)
        last_recorded_mood = UserMood.objects.filter(user=loged_user).last()

        content = Content.objects.filter(mood=last_recorded_mood.mood)

        random_num = random.randrange(0, content.count())
        random_content = content[random_num]

        dataResponse = {
            'msg': f'user {request.user.username} content after emotion analysis',
            'content': ContentSerializer(instance=random_content).data }
        return Response(dataResponse, status=status.HTTP_200_OK)

    else:
        dataResponse = {'msg': 'unathurazed access'}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)

# helper function
def add_userMood(user_id, PickleFile):
     '''
     this method is being called by mood prediction API  to add 'dominant_emotion into user_mood table
     '''
     print(PickleFile['dominant_emotion'])
     print(user_id)
     #get user and mood
     loged_user = User.objects.get(id = user_id)
     new_mood = Mood.objects.get(name = PickleFile['dominant_emotion'])
     # crreat and add into  user mood
     user_mood = UserMood.objects.create(user=loged_user, mood=new_mood)

