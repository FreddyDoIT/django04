# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2017-02-23 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20170222_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=100, verbose_name='Sevens'),
        ),
        migrations.AlterField(
            model_name='article',
            name='last_update_timestamp',
            field=models.DateTimeField(auto_now=True, verbose_name='文章更新时刻'),
        ),
    ]