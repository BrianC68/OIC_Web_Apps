# Generated by Django 2.2.1 on 2020-02-21 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_payment_square_receipt'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ['-date']},
        ),
    ]
