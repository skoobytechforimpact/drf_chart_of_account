# Generated by Django 2.2.16 on 2020-10-16 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_chart_of_account', '0022_auto_20201016_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layerfivemodel',
            name='ref_no',
            field=models.CharField(default='e9eabc14-abb0-416d-98b0-3afc345dd116', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layerfourmodel',
            name='ref_no',
            field=models.CharField(default='e9eabc14-abb0-416d-98b0-3afc345dd116', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layeronemodel',
            name='ref_no',
            field=models.CharField(default='e9eabc14-abb0-416d-98b0-3afc345dd116', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layerthreemodel',
            name='ref_no',
            field=models.CharField(default='e9eabc14-abb0-416d-98b0-3afc345dd116', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layertwomodel',
            name='ref_no',
            field=models.CharField(default='e9eabc14-abb0-416d-98b0-3afc345dd116', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
    ]