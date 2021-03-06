# Generated by Django 2.0.5 on 2018-05-24 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NobleRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('equivalence', models.CharField(max_length=100)),
                ('honorific', models.TextField()),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('str', models.IntegerField()),
                ('dex', models.IntegerField()),
                ('con', models.IntegerField()),
                ('int', models.IntegerField()),
                ('wis', models.IntegerField()),
                ('cha', models.IntegerField()),
                ('notes', models.TextField()),
                ('awards', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Award')),
                ('gender', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='people.Gender')),
                ('noble_rank', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='people.NobleRank')),
            ],
        ),
    ]
