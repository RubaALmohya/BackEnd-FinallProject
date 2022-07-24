from rest_framework import serializers
from .models import *

class MoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mood
        fields = "__all__"

class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ['img','video','description']

