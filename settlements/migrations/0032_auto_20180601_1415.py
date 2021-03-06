# Generated by Django 2.0.5 on 2018-06-01 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settlements', '0031_stronghold_polity'),
    ]

    operations = [
        migrations.CreateModel(
            name='StrongholdType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='stronghold',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='stronghold',
            name='name',
        ),
        migrations.RemoveField(
            model_name='stronghold',
            name='settlement',
        ),
        migrations.AddField(
            model_name='stronghold',
            name='building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stronghold', related_query_name='stronghold', to='settlements.Building'),
        ),
        migrations.AddField(
            model_name='stronghold',
            name='custom_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
