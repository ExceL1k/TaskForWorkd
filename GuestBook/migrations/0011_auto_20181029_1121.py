# Generated by Django 2.1.2 on 2018-10-29 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuestBook', '0010_bookguest_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookguest',
            name='img',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
