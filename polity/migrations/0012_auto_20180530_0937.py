# Generated by Django 2.0.5 on 2018-05-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polity', '0011_auto_20180527_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='polity',
            name='fame',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='polity',
            name='infamy',
            field=models.IntegerField(default=0),
        ),
    ]
