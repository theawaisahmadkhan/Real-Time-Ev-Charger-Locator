# Generated by Django 4.1.8 on 2023-06-14 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evchargingapp', '0007_userbill'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbill',
            name='rating',
            field=models.IntegerField(default=None, max_length=10, null=True),
        ),
    ]
