from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserCredentialSerializer(serializers.ModelSerializer):
    '''
         Translated the model instance into Python native datatypes.
         To finalise the serialization process we render the 'UserCredential Model'  data into json
        '''
    pic = serializers.SerializerMethodField(required=False)

    class Meta:
        model = UserCredential
        fields = '__all__'


    def get_pic(self, record: UserCredential):
        return record.pic


class UserSerializer(serializers.ModelSerializer):
    '''
     Translated the model instance into Python native datatypes.
     To finalise the serialization process we render the 'User Model'  data into json
    '''
 #   user_credential = UserCredentialSerializer()

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name', 'password']

'''    def create(self, validated_data):
        user_credential = validated_data.pop('user_credential')
        user_instance = User.objects.create(**validated_data)

        UserCredential.objects.create(user=user_instance)
        return user_instance'''

