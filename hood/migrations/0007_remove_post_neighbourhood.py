# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-31 07:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0006_auto_20191031_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='neighbourhood',
        ),
    ]