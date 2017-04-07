# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 06:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0009_auto_20170315_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='classify',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Model.Category'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Model.State'),
        ),
        migrations.AlterField(
            model_name='mes',
            name='floor',
            field=models.IntegerField(default=1, verbose_name='\u697c\u5c42'),
        ),
    ]
