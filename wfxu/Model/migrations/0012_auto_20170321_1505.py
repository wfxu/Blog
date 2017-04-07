# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 07:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0011_auto_20170316_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='digest',
            field=models.CharField(default='\u6458\u8981', max_length=200, verbose_name='\u6458\u8981'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='classify',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Model.Category'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.ForeignKey(default='publication', on_delete=django.db.models.deletion.CASCADE, to='Model.State'),
        ),
    ]
