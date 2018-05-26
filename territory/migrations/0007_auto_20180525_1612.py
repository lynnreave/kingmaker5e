# Generated by Django 2.0.5 on 2018-05-25 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territory', '0006_auto_20180525_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='territory',
            name='features',
            field=models.ManyToManyField(blank=True, related_name='territory', related_query_name='territories', to='territory.Feature'),
        ),
        migrations.AlterField(
            model_name='territory',
            name='improvements',
            field=models.ManyToManyField(blank=True, related_name='territory', related_query_name='territories', to='territory.Improvement'),
        ),
    ]
