# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 01:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('classify', models.CharField(max_length=10, verbose_name='\u5206\u7c7b')),
                ('status', models.CharField(max_length=5, verbose_name='\u72b6\u6001')),
                ('toptime', models.DateTimeField(auto_now_add=True, verbose_name='\u65f6\u95f4')),
                ('content', tinymce.models.HTMLField(verbose_name='\u6587\u7ae0')),
            ],
        ),
        migrations.CreateModel(
            name='Mes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500, verbose_name='\u4fe1\u606f')),
                ('mestime', models.DateTimeField(auto_now_add=True, verbose_name='\u65f6\u95f4')),
                ('topmes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Model.Blog')),
            ],
        ),
    ]
