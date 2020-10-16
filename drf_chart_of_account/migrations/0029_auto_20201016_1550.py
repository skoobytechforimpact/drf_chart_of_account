# Generated by Django 3.0.10 on 2020-10-16 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_chart_of_account', '0028_auto_20201016_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layerfivemodel',
            name='ref_no',
            field=models.CharField(default='f653178c-fbdd-4660-9c2d-91b9e2561328', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layerfourmodel',
            name='ref_no',
            field=models.CharField(default='f653178c-fbdd-4660-9c2d-91b9e2561328', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layeronemodel',
            name='ref_no',
            field=models.CharField(default='f653178c-fbdd-4660-9c2d-91b9e2561328', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layerthreemodel',
            name='ref_no',
            field=models.CharField(default='f653178c-fbdd-4660-9c2d-91b9e2561328', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layertwomodel',
            name='ref_no',
            field=models.CharField(default='f653178c-fbdd-4660-9c2d-91b9e2561328', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
    ]