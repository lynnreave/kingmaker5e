# Generated by Django 2.0.5 on 2018-06-01 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polity', '0013_logentry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logentry',
            old_name='text',
            new_name='log',
        ),
        migrations.RemoveField(
            model_name='logentry',
            name='name',
        ),
    ]
