from django.db import models
from django.contrib.auth.models import User
import datetime

class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateField(default=datetime.date.today)
    verse = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
