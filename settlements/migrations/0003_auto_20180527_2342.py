# Generated by Django 2.0.5 on 2018-05-28 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settlements', '0002_auto_20180527_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='magic_common',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='type',
            name='magic_rare',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='type',
            name='magic_uncommon',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
