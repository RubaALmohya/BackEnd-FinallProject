from django.conf import settings
from django.urls import path
from mood_app import views
from django.conf.urls.static import static
urlpatterns = [

    path("TakePhoto/", views.TakePhoto),
    path("pre" , views.EmotionPrediction),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)