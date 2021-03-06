# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 10:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drugtest', '0014_auto_20160725_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultmaster',
            name='medical_technologist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='MedTech', to='drugtest.Staff'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resultmaster',
            name='pathologist',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='Pathologist', to='drugtest.Staff'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='license',
            field=models.CharField(blank=True, default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='staff',
            name='designation',
            field=models.SmallIntegerField(choices=[(1, 'Medical Technologist'), (2, 'Pathologist')], default=1),
        ),
    ]
