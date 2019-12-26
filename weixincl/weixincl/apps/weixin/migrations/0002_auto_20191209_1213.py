# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-12-09 04:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weixin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collecttask',
            name='task_status',
            field=models.SmallIntegerField(choices=[(2, '抓取中'), (1, '未抓取'), (3, '抓取完成')], default=1, verbose_name='任务状态'),
        ),
    ]
