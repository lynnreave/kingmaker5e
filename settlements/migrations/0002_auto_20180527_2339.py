# Generated by Django 2.0.5 on 2018-05-28 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settlements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='con_bonus',
            field=models.FloatField(),
        ),
    ]
