# Generated by Django 2.0.5 on 2018-05-30 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armed_forces', '0017_boon'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialAbility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='armedforce',
            name='special_abilities',
            field=models.ManyToManyField(blank=True, related_name='armed_force', related_query_name='armed_force', to='armed_forces.SpecialAbility'),
        ),
    ]
