# Generated by Django 2.0.5 on 2018-05-30 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20180527_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='fame_increment',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='infamy_increment',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='treasury_increment',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='unrest_increment',
            field=models.IntegerField(default=0),
        ),
    ]
