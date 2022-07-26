from django.conf import settings

from . import views
from django.urls import path


from django.conf.urls.static import static
urlpatterns = [
    path('user_moods/', views.user_moods, name='user_moods'),
    path("take_photo/", views.TakePhoto, name='take_photo'),
    path("mood_prediction/" , views.EmotionPrediction, name='mood_prediction'),
    path('display_content/', views.display_content, name='display_content')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)