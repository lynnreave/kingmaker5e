# Generated by Django 2.0.5 on 2018-05-27 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polity', '0004_auto_20180527_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='alignmentge',
            name='cor_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alignmentge',
            name='cri_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alignmentge',
            name='eco_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alignmentge',
            name='fam_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alignmentge',
            name='inf_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alignmentge',
            name='law_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alignmentge',
            name='lor_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alignmentge',
            name='loy_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alignmentge',
            name='pro_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alignmentge',
            name='soc_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alignmentge',
            name='sta_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alignmentlc',
            name='cor_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alignmentlc',
            name='cri_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alignmentlc',
            name='eco_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alignmentlc',
            name='fam_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alignmentlc',
            name='inf_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alignmentlc',
            name='law_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alignmentlc',
            name='lor_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alignmentlc',
            name='loy_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alignmentlc',
            name='pro_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alignmentlc',
            name='soc_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alignmentlc',
            name='sta_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='government',
            name='cor_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='government',
            name='cri_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='government',
            name='eco_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='government',
            name='fam_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='government',
            name='inf_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='government',
            name='law_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='government',
            name='lor_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='government',
            name='loy_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='government',
            name='pro_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='government',
            name='soc_bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='government',
            name='sta_bonus',
            field=models.IntegerField(default=0),
        ),
    ]