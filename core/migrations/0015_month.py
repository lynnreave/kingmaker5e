# Generated by Django 2.0.5 on 2018-06-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_recruitmentedict_armed_forces_mult'),
    ]

    operations = [
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('equivalent', models.CharField(max_length=100)),
            ],
        ),
    ]
