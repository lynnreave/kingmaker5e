# Generated by Django 2.0.5 on 2018-05-26 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polity',
            name='desc',
            field=models.TextField(blank=True, default=''),
        ),
    ]
