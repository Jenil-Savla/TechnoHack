# Generated by Django 3.2.8 on 2022-02-18 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_longitute_location_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='guardian',
            name='favourite',
            field=models.BooleanField(default=False),
        ),
    ]
