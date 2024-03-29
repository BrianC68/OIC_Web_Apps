# Generated by Django 2.2.23 on 2021-10-22 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('how_to_videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['video_category'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=None, max_length=100),
        ),
    ]
