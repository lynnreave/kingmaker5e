# Generated by Django 2.0.5 on 2018-05-29 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armed_forces', '0002_auto_20180529_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldiertype',
            name='default_cr',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AddField(
            model_name='unittype',
            name='acr_mod',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='unittype',
            name='camo_mod',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='unittype',
            name='equip_cost_mult',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='unittype',
            name='num_soldiers',
            field=models.IntegerField(default=1),
        ),
    ]