# Generated by Django 2.2.16 on 2020-10-15 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_chart_of_account', '0015_auto_20201015_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layerfivemodel',
            name='ref_no',
            field=models.CharField(default='eac7f4c1-d447-4384-bc4c-fbcb883b5635', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layerfourmodel',
            name='ref_no',
            field=models.CharField(default='eac7f4c1-d447-4384-bc4c-fbcb883b5635', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layeronemodel',
            name='ref_no',
            field=models.CharField(default='eac7f4c1-d447-4384-bc4c-fbcb883b5635', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layerthreemodel',
            name='ref_no',
            field=models.CharField(default='eac7f4c1-d447-4384-bc4c-fbcb883b5635', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layertwomodel',
            name='ref_no',
            field=models.CharField(default='eac7f4c1-d447-4384-bc4c-fbcb883b5635', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
    ]