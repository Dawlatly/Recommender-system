# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-17 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20170917_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_Name', models.CharField(max_length=50)),
            ],
        ),
    ]
