# Generated by Django 2.2.1 on 2020-08-28 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bald_eagles', '0002_auto_20200827_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baldeaglessession',
            name='skater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
