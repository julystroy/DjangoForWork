# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-21 05:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automatic', '0002_auto_20171221_1145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('can_access_search_table_list', '可以访问数据查询功能页面'), ('can_change_avatar', '可以修改用户头像')), 'verbose_name_plural': '账户表'},
        ),
    ]
