# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 08:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bookmis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='categoryID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bookmis.BookCategory'),
        ),
    ]
