# Generated by Django 3.1 on 2020-08-20 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0015_auto_20200820_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='liked',
            field=models.BooleanField(default=False),
        ),
    ]