from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from mood_app.serializers import MoodSerializer

class UserMoodSerializer(serializers.ModelSerializer):
    pic = serializers.SerializerMethodField(required=False)
    moods = MoodSerializer(many=True)

    class Meta:
        model = UserMood
        fields = '__all__'

'''    def get_user_moods(self, record: UserMood):
        return record.moods'''


class UserSerializer(serializers.ModelSerializer):
    user_mood = UserMoodSerializer()

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name', 'password', 'user_mood']

    def create(self, validated_data):
        user_mood = validated_data.pop('user_mood')
        user_instance = User.objects.create(**validated_data)

        user_mood.objects.create(user=user_instance,pic= user_mood['pic'], moods=user_mood['moods'])
        return user_instance