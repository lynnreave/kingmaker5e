# Generated by Django 2.0.5 on 2018-05-27 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_recruitmentedict'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitmentedict',
            name='elites_mult',
            field=models.FloatField(),
        ),
    ]
