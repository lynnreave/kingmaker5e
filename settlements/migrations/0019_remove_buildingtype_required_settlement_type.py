# Generated by Django 2.0.5 on 2018-05-28 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settlements', '0018_auto_20180528_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buildingtype',
            name='required_settlement_type',
        ),
    ]
