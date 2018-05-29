# Generated by Django 2.0.5 on 2018-05-28 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polity', '0011_auto_20180527_1651'),
        ('people', '0011_auto_20180527_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='polity',
        ),
        migrations.AddField(
            model_name='person',
            name='polity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='person', related_query_name='person', to='polity.Polity'),
            preserve_default=False,
        ),
    ]