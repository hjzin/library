# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookmis', '0013_remove_borrow_booknum'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='booknum',
            field=models.IntegerField(default=0),
        ),
    ]
