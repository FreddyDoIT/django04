# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2017-02-21 10:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='block',
            old_name='admin_name',
            new_name='admin',
        ),
    ]
