# Generated by Django 2.0.5 on 2018-05-26 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polity', '0002_auto_20180525_2237'),
        ('people', '0008_auto_20180525_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='polity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='person', related_query_name='person', to='polity.Polity'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='awards',
            field=models.ManyToManyField(blank=True, related_name='person', related_query_name='person', to='people.Award'),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person', related_query_name='person', to='people.Gender'),
        ),
        migrations.AlterField(
            model_name='person',
            name='noble_rank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person', related_query_name='person', to='people.NobleRank'),
        ),
    ]
