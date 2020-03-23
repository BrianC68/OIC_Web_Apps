# Generated by Django 2.2.1 on 2020-03-20 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('figure_skating', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='figureskatingsession',
            options={'ordering': ['-session__skate_date']},
        ),
        migrations.AlterUniqueTogether(
            name='figureskatingsession',
            unique_together={('skater', 'session')},
        ),
    ]
