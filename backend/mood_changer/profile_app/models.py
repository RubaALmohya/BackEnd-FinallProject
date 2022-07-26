from django.db import models
from django.contrib.auth.models import User
from mood_app.models import Content

excellent, good, neutral, bad, relly_bad = 5,4,3,2,1
RATING_CHOICES = [
        (excellent, 5),
        (good, 4),
        (neutral, 3),
        (bad, 2),
        (relly_bad, 1),
]

class Rating (models.Model):
    '''
    this model for user rating after mood diagnostic
    '''
    user = models.ForeignKey(User, related_name='user_rating',on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES,default=5)

class Favorite(models.Model):
    '''
    this model for user Favorite Content
    '''
    user = models.ForeignKey(User, related_name= 'User_fave',on_delete=models.CASCADE)
    Content = models.ForeignKey(Content, related_name= 'fav_content',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)




