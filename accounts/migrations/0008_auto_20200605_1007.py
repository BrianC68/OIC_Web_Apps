# Generated by Django 2.2.1 on 2020-06-05 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200605_0826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='release_of_liability',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='release_of_liability_date_signed',
        ),
    ]
