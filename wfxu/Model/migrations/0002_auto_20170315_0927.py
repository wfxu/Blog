# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 01:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Model', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mes',
            old_name='topmes',
            new_name='conmes',
        ),
    ]
