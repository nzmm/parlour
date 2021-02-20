# Generated by Django 3.1.7 on 2021-02-20 19:02

from os import environ
from django.db import migrations
from django.contrib.auth.models import User


def init_default_superuser(apps, schema_editor):
    username, pwd, email = environ['ROOT_USER'], environ['ROOT_PASSWORD'], environ['ROOT_EMAIL']

    if User.objects.filter(username=username, is_superuser=True).exists():
        print("Superuser with default username already exists.")
        return

    su = User.objects.create_superuser(username, password=pwd, email=email)
    su.save()
    return

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '__latest__'),
        ('server', '0004_auto_20200915_0620'),
    ]

    operations = [
        migrations.RunPython(init_default_superuser),
    ]