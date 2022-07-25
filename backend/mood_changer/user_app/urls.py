from django.conf import settings
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

app_name = 'user_app'

urlpatterns = [
   path('register/', views.register, name='register'),
   path('login/', views.login, name='login'),
   path('logout/', auth_views.LogoutView.as_view, name='logout'), # built in views for logout
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)