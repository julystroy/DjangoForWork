# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-09-06 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0024_auto_20170906_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='register_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='注册时间'),
        ),
    ]
