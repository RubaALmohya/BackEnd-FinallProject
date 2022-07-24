from django.db import models
from django.contrib.auth.models import User
from mood_app.models import Mood

class UserCredential(models.Model):
    '''
     this model contains the Many-to-Many relationship.
     It add another attrib to auth.model.user: from model mood.
    '''
    user = models.OneToOneField(User, related_name= 'user_credential',on_delete=models.CASCADE, null=True)
    pic = models.ImageField(upload_to="media/images/user_profile_pic")

class UserMood(models.Model):
    '''
    this model contains the one-to-one relationship.
    Select the user and the user's mood
    '''
    user = models.ForeignKey(UserCredential, related_name= 'user_credential',on_delete=models.CASCADE)
    mood = models.ForeignKey(Mood, related_name= 'User_mood',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

