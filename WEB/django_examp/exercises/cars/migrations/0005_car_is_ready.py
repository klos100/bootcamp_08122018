# Generated by Django 2.1.7 on 2019-03-03 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='is_ready',
            field=models.BooleanField(default=False),
        ),
    ]
