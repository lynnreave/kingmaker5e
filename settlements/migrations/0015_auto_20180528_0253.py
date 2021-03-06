# Generated by Django 2.0.5 on 2018-05-28 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settlements', '0014_auto_20180528_0234'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(blank=True)),
                ('const_cost', models.IntegerField()),
                ('const_time', models.IntegerField()),
                ('lots', models.IntegerField(default=1)),
                ('pop_bonus', models.IntegerField(default=0)),
                ('special', models.TextField(blank=True)),
                ('eco_bonus', models.IntegerField(default=0)),
                ('loy_bonus', models.IntegerField(default=0)),
                ('sta_bonus', models.IntegerField(default=0)),
                ('fam_bonus', models.IntegerField(default=0)),
                ('inf_bonus', models.FloatField(default=0)),
                ('cor_bonus', models.IntegerField(default=0)),
                ('cri_bonus', models.IntegerField(default=0)),
                ('law_bonus', models.IntegerField(default=0)),
                ('lor_bonus', models.IntegerField(default=0)),
                ('pro_bonus', models.IntegerField(default=0)),
                ('soc_bonus', models.IntegerField(default=0)),
                ('def_bonus', models.IntegerField(default=0)),
                ('con_bonus', models.IntegerField(default=0)),
                ('inc_bonus', models.IntegerField(default=0)),
                ('unr_bonus', models.IntegerField(default=0)),
                ('dan_bonus', models.IntegerField(default=0)),
                ('limit', models.IntegerField(blank=True, null=True)),
                ('magic_items', models.CharField(blank=True, max_length=300, null=True)),
                ('discounts', models.ManyToManyField(blank=True, related_name='_buildingtype_discounts_+', related_query_name='discounted_from', to='settlements.BuildingType')),
                ('required_settlement_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='building_type', related_query_name='building_type', to='settlements.Type')),
                ('upgrade_to', models.ManyToManyField(blank=True, related_name='_buildingtype_upgrade_to_+', related_query_name='upgrade_from', to='settlements.BuildingType')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placement', models.CharField(max_length=12)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='building',
            name='discounts',
        ),
        migrations.RemoveField(
            model_name='building',
            name='required_settlement_type',
        ),
        migrations.RemoveField(
            model_name='building',
            name='upgrade_to',
        ),
        migrations.DeleteModel(
            name='Building',
        ),
    ]
