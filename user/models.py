from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    friends = models.ManyToManyField(User, related_name="person")

    def __str__(self):
        return self.user.first_name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

# class Friend(models.Model):
#     users = models.ManyToManyField(User)
#     current_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True)
#
