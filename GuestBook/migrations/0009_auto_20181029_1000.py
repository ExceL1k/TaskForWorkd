# Generated by Django 2.1.2 on 2018-10-29 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuestBook', '0008_auto_20181029_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookguest',
            name='ip',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
