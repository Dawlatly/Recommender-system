# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-21 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_auto_20180121_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_Id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
