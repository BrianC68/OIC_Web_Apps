# Generated by Django 2.2.1 on 2020-06-12 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_profile_mike_schultz_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='yeti_skate_email',
            field=models.BooleanField(default=False),
        ),
    ]
