# Generated by Django 2.0.5 on 2018-05-27 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polity', '0009_auto_20180527_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='polity',
            name='treasury',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='polity',
            name='unrest',
            field=models.IntegerField(default=0),
        ),
    ]
