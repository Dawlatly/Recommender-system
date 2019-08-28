# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-01 12:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20180101_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_Id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('cart_Customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.Customer')),
                ('cart_Products', models.ManyToManyField(to='store.Product')),
            ],
        ),
    ]