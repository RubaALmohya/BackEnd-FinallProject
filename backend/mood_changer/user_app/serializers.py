from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserCredentialSerializer(serializers.ModelSerializer):
    pic = serializers.SerializerMethodField(required=False)

    class Meta:
        model = UserCredential
        fields = '__all__'

    '''    
     Translated the model instance into Python native datatypes.
     To finalise the serialization process we render the 'UserCredential Model'  data into json
    '''


class UserSerializer(serializers.ModelSerializer):
    user_credential = UserCredentialSerializer()

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name', 'password', 'user_credential']

    def create(self, validated_data):
        user_credential = validated_data.pop('user_credential')
        user_instance = User.objects.create(**validated_data)

        UserCredential.objects.create(user=user_instance,pic= user_credential['pic'])
        return user_instance

    '''    
     Translated the model instance into Python native datatypes.
     To finalise the serialization process we render the 'User Model'  data into json
    '''
