from django.db import models

class Mood(models.Model):
    '''
    this model contains the different moods info relationship.
    '''
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=25)
    date = models.DateTimeField(auto_now=True)