# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 06:32
from __future__ import unicode_literals

from django.db import migrations
from django.core.management import call_command

fixture = 'initial_data'

def load_initial(apps, schema_editor):
    # call_command('loaddata', fixture, app_label='drugtest')
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('drugtest', '0007_merge'),
    ]

    operations = [
        migrations.RunPython(load_initial)
    ]
