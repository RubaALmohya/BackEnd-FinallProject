from django.contrib import admin
<<<<<<< HEAD
from .models import UserMood ,UserCredential
=======
from .models import *
>>>>>>> 9c643b7e2c76c854bc19f8f054fd23a62f33d273

class UserMoodAdmin(admin.ModelAdmin):
  list_display = ('id', 'user')

admin.site.register(UserMood, UserMoodAdmin)
<<<<<<< HEAD
admin.site.register(UserCredential)
=======
admin.site.register(UserCredential)
>>>>>>> 9c643b7e2c76c854bc19f8f054fd23a62f33d273
