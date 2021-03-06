# Generated by Django 2.1.4 on 2019-01-11 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('desc', models.TextField(blank=True, max_length=50)),
                ('bible_ver', models.CharField(choices=[('ASV', 'The Holy Bible, American Standard Version Bible'), ('engDRA', 'Douay-Rheims American 1899 The Holy Bible in English, Douay-Rheims American Edition of 1899, translated from the Latin Vulgate'), ('enggnv', 'Geneva Bible common'), ('enKJVe', 'King James (Authorised) Version Ecumenical'), ('enKJVp', 'King James (Authorised) Version Protestant'), ('engojp', 'JPS TaNaKH 1917 Jewish'), ('engRV', 'Revised Version 1885 Interconfessional'), ('GNT', 'Good News Translation Protestant Bible'), ('GNTD', 'Good News Translation (US Version) Catholic Interconfessional Bible'), ('T4T', 'Translation for Translators common'), ('WEBE', 'World English Bible Ecumenical'), ('WEBC', 'World English Bible Catholic'), ('WEBO', 'World English Bible Orthodox'), ('WEBP', 'World English Bible Protestant'), ('WEBBEE', 'World English Bible British Edition Ecumenical'), ('WEBBEC', 'World English Bible British Edition Catholic'), ('WEBBEO', 'World English Bible British Edition Orthodox'), ('WEBBEP', 'World English Bible British Edition Protestant'), ('WMB', 'World Messianic Bible Messianic'), ('WMBBEM', 'World Messianic Bible British Edition Messianic')], default='WEBP', max_length=6)),
                ('friends', models.ManyToManyField(related_name='person', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
