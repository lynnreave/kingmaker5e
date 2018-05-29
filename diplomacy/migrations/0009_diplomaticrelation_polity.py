# Generated by Django 2.0.5 on 2018-05-28 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polity', '0011_auto_20180527_1651'),
        ('diplomacy', '0008_auto_20180527_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='diplomaticrelation',
            name='polity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='diplomatic_relation', related_query_name='diplomatic_relation', to='polity.Polity'),
        ),
    ]