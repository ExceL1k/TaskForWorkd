# Generated by Django 2.1.2 on 2018-10-23 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuestBook', '0005_auto_20181023_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookguest',
            name='cashBrowser',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
