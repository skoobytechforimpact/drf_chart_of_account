# Generated by Django 2.1.15 on 2020-10-16 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_chart_of_account', '0026_auto_20201016_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layerfivemodel',
            name='ref_no',
            field=models.CharField(default='2f7c7b67-c216-4c8c-ade0-e85b5445d69e', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layerfourmodel',
            name='ref_no',
            field=models.CharField(default='2f7c7b67-c216-4c8c-ade0-e85b5445d69e', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layeronemodel',
            name='ref_no',
            field=models.CharField(default='2f7c7b67-c216-4c8c-ade0-e85b5445d69e', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layerthreemodel',
            name='ref_no',
            field=models.CharField(default='2f7c7b67-c216-4c8c-ade0-e85b5445d69e', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layertwomodel',
            name='ref_no',
            field=models.CharField(default='2f7c7b67-c216-4c8c-ade0-e85b5445d69e', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
    ]
