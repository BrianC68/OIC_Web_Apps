# Generated by Django 2.2.1 on 2020-08-28 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_profile_bald_eagles_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='lady_hawks_email',
            field=models.BooleanField(default=False),
        ),
    ]