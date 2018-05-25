# Generated by Django 2.0.5 on 2018-05-25 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Improvement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pop_bonus', models.IntegerField(default=0)),
                ('eco_bonus', models.IntegerField(default=0)),
                ('loy_bonus', models.IntegerField(default=0)),
                ('sta_bonus', models.IntegerField(default=0)),
                ('def_bonus', models.IntegerField(default=0)),
                ('con_bonus', models.IntegerField(default=0)),
                ('inc_bonus', models.IntegerField(default=0)),
                ('unr_bonus', models.IntegerField(default=0)),
                ('exclusive', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Territory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('features', models.ManyToManyField(related_name='territory', related_query_name='territory', to='territory.Feature')),
                ('improvements', models.ManyToManyField(related_name='territory', related_query_name='territory', to='territory.Improvement')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pop_bonus', models.IntegerField(default=0)),
                ('dan_bonus', models.IntegerField(default=0)),
                ('exp_time', models.IntegerField(default=1, null=True)),
                ('prep_time', models.IntegerField(default=1, null=True)),
                ('prep_cost', models.IntegerField(default=1, null=True)),
                ('farm_cost', models.IntegerField(default=1, null=True)),
                ('road_cost', models.IntegerField(default=1, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='territory',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='territory', related_query_name='territory', to='territory.Type'),
        ),
    ]
