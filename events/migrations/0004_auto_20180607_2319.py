# Generated by Django 2.0.5 on 2018-06-08 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20180530_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='polity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event', related_query_name='event', to='polity.Polity'),
        ),
    ]
