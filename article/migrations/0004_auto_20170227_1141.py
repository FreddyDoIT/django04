# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2017-02-27 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20170223_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, verbose_name='文章标题'),
        ),
    ]