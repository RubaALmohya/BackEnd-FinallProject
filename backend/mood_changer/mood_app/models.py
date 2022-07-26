from django.db import models

class Mood(models.Model):
    '''
    this model contains the different moods info relationship.
    '''
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Content(models.Model):
    '''
    This model contains the media for each mood
    '''
    mood = models.ForeignKey(Mood, related_name= 'content_mood',on_delete=models.CASCADE)
    img = models.URLField(null=True)
    video = models.URLField(null=True )
    description = models.CharField(max_length=450, null=True)

