# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-21 06:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automatic', '0007_auto_20171221_1440'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('can_access_search_table_list', '可以访问数据查询功能页面'), ('can_change_avatar', '可以修改用户头像'), ('can_access_automatic_index', '可以访问自动化后台首页'), ('can_access_kind_admin_userprofile_table', '可以通过kind_admin插件访问账户表'), ('can_access_kind_admin_userprofile_table_change', '可以通过kind_admin插件访问账户表信息修改页'), ('can_change_kind_admin_userprofile_table', '可以通过kind_admin插件修改账户表信息'), ('can_access_kind_admin_table_index', '可以通过kind_admin插件访问APP库即展示所有注册的model'), ('can_access_kind_admin_all_table_objs', '可以访问kind_admin插件下注册的所有table'), ('can_change_kind_admin_all_table_objs', '可以修改kind_admin插件下注册的所有table'), ('can_change_own_password', '可以修改自己账号的密码')), 'verbose_name_plural': '账户表'},
        ),
    ]
