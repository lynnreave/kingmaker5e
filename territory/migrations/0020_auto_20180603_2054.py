# Generated by Django 2.0.5 on 2018-06-04 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('territory', '0019_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='territory',
            name='map',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='territory', related_query_name='territory', to='territory.Map'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='territory',
            name='hex',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
