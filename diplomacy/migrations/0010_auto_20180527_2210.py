# Generated by Django 2.0.5 on 2018-05-28 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diplomacy', '0009_diplomaticrelation_polity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diplomaticrelation',
            old_name='polity',
            new_name='holder',
        ),
        migrations.RenameField(
            model_name='diplomaticrelation',
            old_name='name',
            new_name='target',
        ),
    ]