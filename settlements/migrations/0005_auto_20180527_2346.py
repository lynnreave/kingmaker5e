# Generated by Django 2.0.5 on 2018-05-28 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settlements', '0004_auto_20180527_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='max_lots',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
