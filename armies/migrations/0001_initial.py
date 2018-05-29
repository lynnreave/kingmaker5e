# Generated by Django 2.0.5 on 2018-05-29 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('polity', '0011_auto_20180527_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Army',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('polity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='army', related_query_name='army', to='polity.Polity')),
            ],
        ),
    ]
