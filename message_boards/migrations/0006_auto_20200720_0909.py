# Generated by Django 2.2.1 on 2020-07-20 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message_boards', '0005_auto_20200717_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
    ]
