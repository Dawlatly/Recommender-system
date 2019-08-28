# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-22 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_order_order_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='zipcode',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(default='', max_length=50),
        ),
    ]
