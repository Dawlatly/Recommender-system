# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-16 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='confirm_password',
            field=models.CharField(default='', max_length=50),
        ),
    ]
