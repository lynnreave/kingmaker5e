# Generated by Django 2.0.5 on 2018-05-28 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settlements', '0013_settlement'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='discounts',
            field=models.ManyToManyField(blank=True, related_name='_building_discounts_+', related_query_name='discounted_from', to='settlements.Building'),
        ),
        migrations.AddField(
            model_name='building',
            name='upgrade_to',
            field=models.ManyToManyField(blank=True, related_name='_building_upgrade_to_+', related_query_name='upgrade_from', to='settlements.Building'),
        ),
    ]
