# Generated by Django 2.0.5 on 2018-06-08 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0007_auto_20180531_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traderoute',
            name='success_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trade_route', related_query_name='trade_route', to='trade.SuccessLevel'),
        ),
    ]