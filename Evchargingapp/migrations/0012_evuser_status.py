# Generated by Django 4.1.8 on 2023-07-01 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evchargingapp', '0011_booking_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='evuser',
            name='status',
            field=models.CharField(default='Yes', max_length=255),
        ),
    ]