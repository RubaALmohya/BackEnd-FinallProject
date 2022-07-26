from django.conf import settings
from django.urls import path
from  . import views
from django.conf.urls.static import static

app_name = 'profile_app'

urlpatterns = [
                path('get_user_info/' ,views.get_user_info, name='get_user_info' ),
                path('add_user_fav/<content_id>', views.add_user_fav, name='add_user_fav'),
                path('get_user_fav/', views.get_user_fav, name='get_user_fav'),
                path('delete_uers_fav/<fav_id>', views.delete_uers_fav, name='delete_uers_fav'),
                path('add_rating/', views.add_rating, name='add_rating'),
                path('get_overall_rating_AVG/', views.get_overall_rating_AVG, name='get_overall_rating_AVG'),
                path('get_user_rating_avg/', views.get_user_rating_avg, name='get_user_rating_avg')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)