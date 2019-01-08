from django.db import models
from django.contrib.auth.models import User
import datetime


class Reading(models.Model):
    date = models.PositiveSmallIntegerField()
    r = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.r


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateField(default=datetime.date.today)
    verse = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    reading = models.ForeignKey(Reading, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Progress(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE)
    reading = models.ForeignKey(Reading, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.status)
