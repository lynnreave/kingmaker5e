# Generated by Django 2.0.5 on 2018-05-28 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diplomacy', '0004_auto_20180527_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='attitude',
            name='step',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='diplomaticrelation',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
