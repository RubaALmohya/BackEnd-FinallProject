from django.db import models
from django.contrib.auth.models import User
from mood_app.models import Mood

class UserCredential(models.Model):
    '''
     this model add another attrib to auth.model.user via one-to-one relationship
    '''
    user = models.OneToOneField(User, related_name= 'user_credential',on_delete=models.CASCADE, null=True)
    pic = models.URLField()


class UserMood(models.Model):
    '''
    this model represint the many-to-many relationship between user and mood(mood_app) tables
    '''
    user = models.ForeignKey(User, related_name= 'user',on_delete=models.CASCADE)
    mood = models.ForeignKey(Mood, related_name= 'User_mood',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

