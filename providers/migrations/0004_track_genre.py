# Generated by Django 3.1 on 2020-08-19 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0003_auto_20200819_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='genre',
            field=models.CharField(default='', max_length=255),
        ),
    ]
