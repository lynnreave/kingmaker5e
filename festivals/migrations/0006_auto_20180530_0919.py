# Generated by Django 2.0.5 on 2018-05-30 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivals', '0005_type_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='festival',
            name='desc',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='successlevel',
            name='effect_mult',
            field=models.FloatField(default=1.0),
        ),
        migrations.AddField(
            model_name='type',
            name='cri_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='type',
            name='law_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='type',
            name='soc_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='type',
            name='sta_bonus',
            field=models.IntegerField(default=0),
        ),
    ]