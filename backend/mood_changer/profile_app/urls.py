from django.conf import settings
from django.urls import path
from  . import views
from django.conf.urls.static import static
urlpatterns = [
                path('get_user_info/' ,views.get_user_info, name='get_user_info' ),
                path('add_user_fav/<content_id>', views.add_user_fav, name='add_user_fav'),
                path('get_user_fav/', views.get_user_fav, name='get_user_fav2'),
                path('delete_uers/<fav_id>', views.delete_uers, name='delete_uers'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)