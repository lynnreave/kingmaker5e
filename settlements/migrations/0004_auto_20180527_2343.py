# Generated by Django 2.0.5 on 2018-05-28 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settlements', '0003_auto_20180527_2342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type',
            old_name='magic_common',
            new_name='magic_items',
        ),
        migrations.RemoveField(
            model_name='type',
            name='magic_rare',
        ),
        migrations.RemoveField(
            model_name='type',
            name='magic_uncommon',
        ),
    ]