# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookmis', '0019_auto_20171209_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='isloss',
            field=models.CharField(default='否', max_length=3),
        ),
    ]
