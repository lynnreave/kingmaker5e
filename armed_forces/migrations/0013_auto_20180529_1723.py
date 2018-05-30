# Generated by Django 2.0.5 on 2018-05-30 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armed_forces', '0012_armedforce_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(blank=True)),
                ('requirements', models.TextField(blank=True)),
                ('cost', models.IntegerField()),
                ('om_mod', models.IntegerField(default=0)),
                ('om_melee_mod', models.IntegerField(default=0)),
                ('om_ranged_mod', models.IntegerField(default=0)),
                ('dv_mod', models.IntegerField(default=0)),
                ('speed_mod', models.IntegerField(default=0)),
                ('morale_mod', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='armedforce',
            name='mount_cr',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
