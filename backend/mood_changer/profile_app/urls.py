from django.conf import settings
from django.urls import path
from  . import views
from django.conf.urls.static import static
urlpatterns = [
                path('get_user_info/' ,views.get_user_info, name='get_user_info' )

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)