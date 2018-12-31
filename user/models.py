from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    bible_versions = (("ASV", "The Holy Bible, American Standard Version Bible"),
                      ("engDRA", "Douay-Rheims American 1899 The Holy Bible in English, Douay-Rheims American Edition of 1899, translated from the Latin Vulgate"),
                      ("enggnv", "Geneva Bible common"),
                      ("enKJVe", "King James (Authorised) Version Ecumenical"),
                      ("enKJVp", "King James (Authorised) Version Protestant"),
                      ("engojp", "JPS TaNaKH 1917 Jewish"),
                      ("engRV", "Revised Version 1885 Interconfessional"),
                      ("GNT", "Good News Translation Protestant Bible"),
                      ("GNTD", "Good News Translation (US Version) Catholic Interconfessional Bible"),
                      ("T4T", "Translation for Translators common"),
                      ("WEBE", "World English Bible Ecumenical"),
                      ("WEBC", "World English Bible Catholic"),
                      ("WEBO", "World English Bible Orthodox"),
                      ("WEBP", "World English Bible Protestant"),
                      ("WEBBEE", "World English Bible British Edition Ecumenical"),
                      ("WEBBEC", "World English Bible British Edition Catholic"),
                      ("WEBBEO", "World English Bible British Edition Orthodox"),
                      ("WEBBEP", "World English Bible British Edition Protestant"),
                      ("WMB", "World Messianic Bible Messianic"),
                      ("WMBBEM", "World Messianic Bible British Edition Messianic"))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    friends = models.ManyToManyField(User, related_name="person")
    bible_ver = models.CharField(max_length=6, choices=bible_versions, default="WEBP")

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
