from django.db import models
from django.contrib.auth.models import User
from mood_app.models import Mood

class UserMood(models.Model):
    '''
     this model contains the Many-to-Many relationship.
     It add another attrib to auth.model.user: from model mood.
    '''
    user = models.OneToOneField(User, related_name= 'user_mood',on_delete=models.CASCADE, null=True)
    pic = models.ImageField(upload_to="images/user_profile_pic", related_name= 'user_pic')
    moods = models.ManyToManyField(Mood, related_name= 'user_moods',on_delete=models.CASCADE, null=True)
