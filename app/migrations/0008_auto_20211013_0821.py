# Generated by Django 2.2 on 2021-10-13 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_cardetails_rear_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardetails',
            name='dash_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='cardetails',
            name='logo_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
