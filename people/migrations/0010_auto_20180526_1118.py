# Generated by Django 2.0.5 on 2018-05-26 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0009_auto_20180525_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeadershipRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ranking', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='leadership_role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person', related_query_name='person', to='people.LeadershipRole'),
        ),
    ]