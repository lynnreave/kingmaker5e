# Generated by Django 2.0.5 on 2018-05-25 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territory', '0002_auto_20180525_0245'),
    ]

    operations = [
        migrations.AddField(
            model_name='territory',
            name='hex',
            field=models.CharField(max_length=20, null=True),
        ),
    ]