# Generated by Django 2.0.5 on 2018-05-26 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_auto_20180524_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='award',
            name='person',
        ),
        migrations.AddField(
            model_name='person',
            name='awards',
            field=models.ManyToManyField(blank=True, null=True, related_name='person', related_query_name='people', to='people.Award'),
        ),
    ]
