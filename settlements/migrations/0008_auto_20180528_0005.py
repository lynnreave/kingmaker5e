# Generated by Django 2.0.5 on 2018-05-28 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settlements', '0007_auto_20180528_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='special',
            field=models.TextField(blank=True),
        ),
    ]