# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-04 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0036_auto_20170928_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otherinfo',
            name='Rplan_recover_account',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='R计划在贷金额'),
        ),
    ]
