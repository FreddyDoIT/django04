# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2017-03-15 11:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('article', '0006_article_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=10000, verbose_name='评论内容')),
                ('status', models.IntegerField(choices=[(0, '正常'), (-1, '删除')], default=0, verbose_name='状态')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='评论创建时间')),
                ('last_update_timestamp', models.DateTimeField(auto_now=True, verbose_name='评论更新时刻')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article', verbose_name='所评论文章')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论作者')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
    ]
