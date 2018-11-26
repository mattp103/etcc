from django.contrib import admin
from .models import UserProfile

class ProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    filter_horizontal = ('friends',)

admin.site.register(UserProfile, ProfileAdmin)
