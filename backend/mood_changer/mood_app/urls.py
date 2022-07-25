from django.conf import settings

from . import views
from django.urls import path


from django.conf.urls.static import static
urlpatterns = [
    path('user_moods/', views.user_moods, name='user_moods'),
    path("TakePhoto/", views.TakePhoto),
    path("pre" , views.EmotionPrediction),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)