# Generated by Django 2.0.5 on 2018-06-08 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('festivals', '0006_auto_20180530_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='festival',
            name='polity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='festival', related_query_name='festival', to='polity.Polity'),
        ),
        migrations.AlterField(
            model_name='festival',
            name='success_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='festival', related_query_name='festival', to='festivals.SuccessLevel'),
        ),
        migrations.AlterField(
            model_name='festival',
            name='target_hex',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='festival', related_query_name='festival', to='territory.Territory'),
        ),
        migrations.AlterField(
            model_name='festival',
            name='target_settlement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='festival', related_query_name='festival', to='settlements.Settlement'),
        ),
    ]