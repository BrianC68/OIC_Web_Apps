# Generated by Django 2.2.1 on 2021-04-11 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('figure_skating', '0004_figureskatingdate_up_down_charge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='figureskater',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
