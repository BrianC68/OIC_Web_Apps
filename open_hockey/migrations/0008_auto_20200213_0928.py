# Generated by Django 2.2.1 on 2020-02-13 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('open_hockey', '0007_auto_20200209_1248'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='openhockeymembertype',
            options={'ordering': ['duration']},
        ),
    ]
