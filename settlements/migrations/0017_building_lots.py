# Generated by Django 2.0.5 on 2018-05-28 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settlements', '0016_auto_20180528_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='lots',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]