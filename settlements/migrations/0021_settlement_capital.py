# Generated by Django 2.0.5 on 2018-05-28 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settlements', '0020_auto_20180528_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='settlement',
            name='capital',
            field=models.BooleanField(default=False),
        ),
    ]