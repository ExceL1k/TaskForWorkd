# Generated by Django 2.1.2 on 2018-10-29 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuestBook', '0007_bookguest_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookguest',
            name='email',
            field=models.EmailField(max_length=60),
        ),
        migrations.AlterField(
            model_name='bookguest',
            name='ip',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AlterField(
            model_name='bookguest',
            name='link',
            field=models.URLField(blank=True, max_length=60, null=True),
        ),
    ]
