# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-22 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_auto_20180121_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='customer',
            name='address2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.CharField(default='', max_length=5),
        ),
    ]
