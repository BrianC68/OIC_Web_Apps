# Generated by Django 2.2.1 on 2021-03-17 14:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0025_profile_chs_alumni_email'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='childskater',
            unique_together={('user', 'first_name', 'last_name')},
        ),
    ]