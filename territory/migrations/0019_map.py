# Generated by Django 2.0.5 on 2018-06-03 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territory', '0018_auto_20180531_2339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]