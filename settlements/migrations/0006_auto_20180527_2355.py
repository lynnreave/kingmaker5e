# Generated by Django 2.0.5 on 2018-05-28 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settlements', '0005_auto_20180527_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='magic_items',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='special',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
