# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugtest', '0013_auto_20160725_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='reference_text',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]