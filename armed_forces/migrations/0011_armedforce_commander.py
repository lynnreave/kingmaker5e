# Generated by Django 2.0.5 on 2018-05-29 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0012_auto_20180527_1919'),
        ('armed_forces', '0010_armedforce_speed'),
    ]

    operations = [
        migrations.AddField(
            model_name='armedforce',
            name='commander',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='armed_force', related_query_name='armed_force', to='people.Person'),
        ),
    ]