# Generated by Django 2.0.5 on 2018-05-29 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armed_forces', '0004_auto_20180529_1421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='armedforce',
            old_name='unit_type',
            new_name='size',
        ),
        migrations.RenameField(
            model_name='armedforce',
            old_name='soldier_type',
            new_name='type',
        ),
    ]