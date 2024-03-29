# Generated by Django 2.2.23 on 2022-02-10 16:12

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
            name='NachoSkateDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skate_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
            options={
                'ordering': ['skate_date'],
                'unique_together': {('skate_date', 'start_time', 'end_time')},
            },
        ),
        migrations.CreateModel(
            name='NachoSkateSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goalie', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False)),
                ('skate_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='session_skaters', to='nacho_skate.NachoSkateDate')),
                ('skater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-skate_date'],
                'unique_together': {('skater', 'skate_date')},
            },
        ),
    ]
