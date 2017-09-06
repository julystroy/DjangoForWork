# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-31 11:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0018_auto_20170829_2048'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assetinfo',
            options={'verbose_name': '资产数据', 'verbose_name_plural': '资产数据'},
        ),
        migrations.AlterModelOptions(
            name='baseinfo',
            options={'verbose_name': '基础数据', 'verbose_name_plural': '基础数据'},
        ),
        migrations.AlterModelOptions(
            name='inviteinfo',
            options={'verbose_name': '邀请数据', 'verbose_name_plural': '邀请数据'},
        ),
        migrations.AlterModelOptions(
            name='kefuinfo',
            options={'verbose_name': '客服数据', 'verbose_name_plural': '客服数据'},
        ),
        migrations.AlterModelOptions(
            name='operateinfo',
            options={'verbose_name': '运营数据', 'verbose_name_plural': '运营数据'},
        ),
        migrations.AlterModelOptions(
            name='qudaoname',
            options={'verbose_name': '渠道名称对应表', 'verbose_name_plural': '渠道名称对应表'},
        ),
        migrations.AlterModelOptions(
            name='tginfo',
            options={'verbose_name': '推广数据', 'verbose_name_plural': '推广数据'},
        ),
        migrations.AlterModelOptions(
            name='wdty_info',
            options={'verbose_name': '网贷天眼数据信息', 'verbose_name_plural': '网贷天眼数据信息'},
        ),
        migrations.AlterModelOptions(
            name='wdzj_info',
            options={'verbose_name': '网贷之家数据信息', 'verbose_name_plural': '网贷之家数据信息'},
        ),
    ]