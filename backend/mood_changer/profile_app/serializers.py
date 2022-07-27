from rest_framework import serializers
from .models import *
from mood_app. serializers import ContentSerializer

class RatingSerializer(serializers.ModelSerializer):
    '''
     Translated the model instance into Python native datatypes.
     To finalise the serialization process we render the 'Rating Model'  data into json
    '''

    class Meta:
        model = Rating
        fields = "__all__"


class FavoriteSerializer(serializers.ModelSerializer):
    '''
     Translated the model instance into Python native datatypes.
     To finalise the serialization process we render the 'Favorite Model'  data into json
    '''
    Content = ContentSerializer()

    class Meta:
        model = Favorite
        fields = ['Content' , 'date']