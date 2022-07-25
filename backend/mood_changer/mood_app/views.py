from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import FileResponse
import joblib
import cv2
from deepface import DeepFace
# Create your views here.


@api_view(['GET'])
def TakePhoto(response):
    '''
    This API is to take the picture from the camera
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
def EmotionPrediction(request):
    '''
    This is an API for classifying and identifying emotion from the captured image using machine learning
    '''

    predictionImg = DeepFace.analyze(photo)
    print(predictionImg)
    print(predictionImg['dominant_emotion'])
    filename = 'takephoto.pkl'
    joblib.dump(predictionImg, filename)
    PickleFile=joblib.load("/Users/user/Downloads/takephoto.pkl")
    userslist = {"msg": "Image Emotion",
                     "details":PickleFile}
    return Response(userslist)
