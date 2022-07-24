from django.contrib import admin
from .models import UserMood

class UserMoodAdmin(admin.ModelAdmin):
  list_display = ('id', 'user')

admin.site.register(UserMood, UserMoodAdmin)
