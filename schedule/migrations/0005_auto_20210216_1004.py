# Generated by Django 2.2.1 on 2021-02-16 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_auto_20191008_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='rinkschedule',
            name='home_locker_room',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='rinkschedule',
            name='visitor_locker_room',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
