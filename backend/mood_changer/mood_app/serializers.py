from rest_framework import serializers
from .models import *

class MoodSerializer(serializers.ModelSerializer):

    '''
     Translated the model instance into Python native datatypes.
     To finalise the serialization process we render the 'Mood Model'  data into json
    '''

    class Meta:
        model = Mood
        fields = "__all__"

class ContentSerializer(serializers.ModelSerializer):
    '''
     Translated the model instance into Python native datatypes.
     To finalise the serialization process we render the 'Content Model'  data into json
    '''

    class Meta:
        model = Content
        fields = ['id', 'img','video','description']

