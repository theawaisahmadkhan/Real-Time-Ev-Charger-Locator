# Generated by Django 4.1.8 on 2023-06-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evchargingapp', '0008_userbill_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('station_id', models.IntegerField()),
                ('bill_id', models.IntegerField()),
                ('rating_number', models.IntegerField()),
            ],
        ),
    ]
