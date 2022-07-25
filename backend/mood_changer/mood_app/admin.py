from django.contrib import admin
from .models import *

class MoodAdmin(admin.ModelAdmin):
  list_display = ('name', 'color')



admin.site.register(Mood, MoodAdmin)
admin.site.register(Content)



