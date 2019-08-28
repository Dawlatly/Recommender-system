# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-21 09:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_auto_20180101_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProducts',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_Products',
        ),
        migrations.AddField(
            model_name='orderproducts',
            name='order_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Order'),
        ),
        migrations.AddField(
            model_name='orderproducts',
            name='product_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product'),
        ),
    ]
