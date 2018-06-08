# Generated by Django 2.0.5 on 2018-06-08 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polity', '0015_auto_20180601_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polity',
            name='ruler_attribute_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='polity_ruler_1', related_query_name='polity_ruler_1', to='polity.Attribute'),
        ),
        migrations.AlterField(
            model_name='polity',
            name='ruler_attribute_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='polity_ruler_2', related_query_name='polity_ruler_2', to='polity.Attribute'),
        ),
        migrations.AlterField(
            model_name='polity',
            name='ruler_attribute_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='polity_ruler_3', related_query_name='polity_ruler_3', to='polity.Attribute'),
        ),
        migrations.AlterField(
            model_name='polity',
            name='spymaster_attribute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='polity_spymaster', related_query_name='polity_spymaster', to='polity.Attribute'),
        ),
    ]
