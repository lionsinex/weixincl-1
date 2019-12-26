# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-12-09 03:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='文章编号')),
                ('publish_time', models.DateTimeField(verbose_name='文章发布时间')),
                ('collect_time', models.DateTimeField(verbose_name='数据采集时间')),
                ('title', models.CharField(default=' ', max_length=50, verbose_name='文章标题')),
                ('author', models.CharField(default=' ', max_length=50, verbose_name='文章作者')),
                ('html_text', models.TextField(default=' ', verbose_name='html内容')),
                ('like_numbers', models.IntegerField(default=1, verbose_name='点赞数')),
                ('content', models.CharField(default=' ', max_length=255, verbose_name='文章内容')),
                ('read_numbers', models.IntegerField(default=1, verbose_name='阅读数')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'db_table': 'tb_articles',
            },
        ),
        migrations.CreateModel(
            name='CollectTask',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(default=' ', max_length=50, verbose_name='任务名称')),
                ('task_status', models.SmallIntegerField(choices=[(3, '抓取完成'), (1, '未抓取'), (2, '抓取中')], default=1, verbose_name='任务状态')),
                ('article_total_count', models.IntegerField(default=0, verbose_name='文章数量')),
                ('_biz', models.CharField(default=' ', max_length=50, verbose_name='_biz')),
                ('task_time', models.DateField(auto_now_add=True, verbose_name='任务创建时间')),
                ('cl_date_start', models.DateField(blank=True, null=True, verbose_name='公众号开始时间')),
                ('cl_date_end', models.DateField(blank=True, null=True, verbose_name='公众号结束时间')),
                ('rl_count', models.BooleanField(default=False, verbose_name='读赞数')),
            ],
            options={
                'verbose_name': '任务',
                'verbose_name_plural': '任务',
                'db_table': 'tb_tasks',
            },
        ),
        migrations.CreateModel(
            name='PublicNum',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='公众号id')),
                ('image_url', models.ImageField(null=True, upload_to='pc_photo', verbose_name='公众号图片')),
                ('weixin_num', models.CharField(default=' ', max_length=50, verbose_name='微信号')),
                ('name', models.CharField(default=' ', max_length=50, verbose_name='公众号名称')),
                ('_biz', models.CharField(default=' ', max_length=255, verbose_name='_biz')),
                ('introduction', models.CharField(default=' ', max_length=255, verbose_name='功能简介')),
            ],
            options={
                'verbose_name': '公众号',
                'verbose_name_plural': '公众号',
                'db_table': 'tb_pc_nums',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='collecttask',
            name='public',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='weixin.PublicNum', verbose_name='公众号'),
        ),
        migrations.AddField(
            model_name='collecttask',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='article',
            name='public_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='weixin.PublicNum', verbose_name='所属公众号'),
        ),
    ]
