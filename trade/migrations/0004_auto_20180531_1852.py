# Generated by Django 2.0.5 on 2018-06-01 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_auto_20180531_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='successlevel',
            name='eco_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='successlevel',
            name='fam_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='successlevel',
            name='fam_increment',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='successlevel',
            name='treasury_increment',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
