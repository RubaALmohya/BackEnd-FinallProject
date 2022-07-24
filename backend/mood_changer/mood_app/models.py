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
    mood = models.ForeignKey(Mood, related_name= 'content_mood',on_delete=models.CASCADE)
    img = models.ImageField(upload_to="media/images/content_mood_img" , null=True)
    video = models.FileField(default = 'xxxx', upload_to="media/video", null=True )
    description = models.CharField(max_length=450)
