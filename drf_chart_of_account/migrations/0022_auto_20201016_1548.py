# Generated by Django 2.1.15 on 2020-10-16 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_chart_of_account', '0021_auto_20201016_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layerfivemodel',
            name='ref_no',
            field=models.CharField(default='8371e0f8-96e2-4520-8999-d9d163dfaa2d', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layerfourmodel',
            name='ref_no',
            field=models.CharField(default='8371e0f8-96e2-4520-8999-d9d163dfaa2d', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layeronemodel',
            name='ref_no',
            field=models.CharField(default='8371e0f8-96e2-4520-8999-d9d163dfaa2d', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layerthreemodel',
            name='ref_no',
            field=models.CharField(default='8371e0f8-96e2-4520-8999-d9d163dfaa2d', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layertwomodel',
            name='ref_no',
            field=models.CharField(default='8371e0f8-96e2-4520-8999-d9d163dfaa2d', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
    ]
