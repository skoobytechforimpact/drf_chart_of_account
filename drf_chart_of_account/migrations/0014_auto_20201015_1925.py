# Generated by Django 2.0.13 on 2020-10-15 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_chart_of_account', '0013_auto_20201015_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layerfivemodel',
            name='ref_no',
            field=models.CharField(default='88635b19-ac36-43f0-b648-1bd2e66260fe', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layerfourmodel',
            name='ref_no',
            field=models.CharField(default='88635b19-ac36-43f0-b648-1bd2e66260fe', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layeronemodel',
            name='ref_no',
            field=models.CharField(default='88635b19-ac36-43f0-b648-1bd2e66260fe', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layerthreemodel',
            name='ref_no',
            field=models.CharField(default='88635b19-ac36-43f0-b648-1bd2e66260fe', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layertwomodel',
            name='ref_no',
            field=models.CharField(default='88635b19-ac36-43f0-b648-1bd2e66260fe', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
    ]
