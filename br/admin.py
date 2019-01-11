from django.contrib import admin
from .models import Comment, Reading, Progress, Notice, readingGroup

admin.site.register(Notice)
admin.site.register(readingGroup)
admin.site.register(Comment)
admin.site.register(Reading)
admin.site.register(Progress)
