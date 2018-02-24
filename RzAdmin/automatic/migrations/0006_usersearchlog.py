# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-24 17:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automatic', '0005_auto_20180222_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSearchLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_name', models.CharField(max_length=32, verbose_name='查询名称')),
                ('condition_dict', models.TextField(verbose_name='查询条件')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='查询时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='查询用户')),
            ],
            options={
                'verbose_name_plural': '用户查询记录日志',
            },
        ),
    ]
