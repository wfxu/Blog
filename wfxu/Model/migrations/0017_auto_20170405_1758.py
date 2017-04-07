# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 09:58
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0016_auto_20170405_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_content', DjangoUeditor.models.UEditorField(verbose_name='\u65e5\u5fd7\u5185\u5bb9')),
                ('log_time', models.DateTimeField(auto_now_add=True, verbose_name='\u65f6\u95f4')),
            ],
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
