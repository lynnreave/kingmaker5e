# Generated by Django 2.0.5 on 2018-06-01 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0004_auto_20180531_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='successlevel',
            name='unrest_increment',
            field=models.IntegerField(default=0),
        ),
    ]
