# Generated by Django 2.2.1 on 2020-06-06 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('figure_skating', '0002_auto_20200320_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='figureskatingdate',
            name='available_spots',
            field=models.IntegerField(default=0),
        ),
    ]