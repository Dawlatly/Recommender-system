# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-17 11:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_customer_confirm_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_Category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='store.Category'),
            preserve_default=False,
        ),
    ]
