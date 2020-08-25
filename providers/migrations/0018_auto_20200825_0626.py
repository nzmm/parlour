# Generated by Django 3.1 on 2020-08-25 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0017_auto_20200824_2015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ('artist__name', 'release_name', 'disc', 'position')},
        ),
        migrations.AddField(
            model_name='release',
            name='provider',
            field=models.CharField(default='graph', max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='release',
            name='provider_id',
            field=models.CharField(default='', max_length=255),
        ),
    ]
