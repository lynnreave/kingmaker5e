# Generated by Django 2.0.5 on 2018-06-01 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settlements', '0039_expansion_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpansionFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
                ('construction_time', models.IntegerField(default=1)),
                ('benefit', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='expansion',
            name='custom_slots',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='expansion',
            name='features',
            field=models.ManyToManyField(blank=True, related_name='expansion', related_query_name='expansion', to='settlements.ExpansionFeature'),
        ),
    ]
