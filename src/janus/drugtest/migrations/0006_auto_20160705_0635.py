# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 06:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugtest', '0005_auto_20160705_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='profiles',
            field=models.ManyToManyField(blank=True, to='drugtest.TestProfile'),
        ),
    ]
