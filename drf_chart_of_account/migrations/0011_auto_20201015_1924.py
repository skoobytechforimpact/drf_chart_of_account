# Generated by Django 2.2.16 on 2020-10-15 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_chart_of_account', '0010_auto_20201015_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layerfivemodel',
            name='ref_no',
            field=models.CharField(default='9f3ed57d-aa1f-42c2-a511-671071826a2a', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layerfourmodel',
            name='ref_no',
            field=models.CharField(default='9f3ed57d-aa1f-42c2-a511-671071826a2a', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layeronemodel',
            name='ref_no',
            field=models.CharField(default='9f3ed57d-aa1f-42c2-a511-671071826a2a', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layerthreemodel',
            name='ref_no',
            field=models.CharField(default='9f3ed57d-aa1f-42c2-a511-671071826a2a', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
        migrations.AlterField(
            model_name='layertwomodel',
            name='ref_no',
            field=models.CharField(default='9f3ed57d-aa1f-42c2-a511-671071826a2a', max_length=80, unique=True, verbose_name='Reference No.'),
        ),
    ]
