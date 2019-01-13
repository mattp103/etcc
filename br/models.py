from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

class Notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField(default=datetime.date.today)

    def __str__(self):
            return self.title


class readingGroup(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=6, unique=True)
    members = models.ManyToManyField(User, related_name="member")
    description = models.TextField(max_length=500)
    tagline = models.TextField(max_length=50)
    notices = models.ManyToManyField(Notice, related_name="announcements")

    def __str__(self):
        return self.title


@receiver(post_save, sender=readingGroup)
def create_group(sender, instance, created, **kwargs):
    if created:
        c =''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVQXYZ0123456789!@#$%^&*(-_=+)')for i in range(6))
        while readingGroup.objects.filter(code=c).exists():
            c =''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVQXYZ0123456789!@#$%^&*(-_=+)')for i in range(6))
        instace.code = c
        instance.save()


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
