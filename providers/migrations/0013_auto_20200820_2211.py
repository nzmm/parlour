# Generated by Django 3.1 on 2020-08-20 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0012_auto_20200820_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='thumbnail_url',
            new_name='thumbnail',
        ),
        migrations.RenameField(
            model_name='release',
            old_name='thumbnail_url',
            new_name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='track',
            name='thumbnail_url',
        ),
        migrations.AddField(
            model_name='track',
            name='thumbnail',
            field=models.CharField(default='', max_length=255),
        ),
    ]