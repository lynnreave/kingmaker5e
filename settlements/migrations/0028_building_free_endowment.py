# Generated by Django 2.0.5 on 2018-05-30 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settlements', '0027_building_endowment'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='free_endowment',
            field=models.BooleanField(default=False),
        ),
    ]
