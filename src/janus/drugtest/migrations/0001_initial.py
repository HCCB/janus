# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 02:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_name', models.CharField(default='', max_length=60)),
                ('family_name', models.CharField(default='', max_length=60)),
                ('middle_name', models.CharField(blank=True, default='', max_length=60)),
                ('birthdate', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
            options={
                'ordering': ('family_name', 'given_name', 'middle_name'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Physician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_name', models.CharField(default='', max_length=60)),
                ('family_name', models.CharField(default='', max_length=60)),
                ('middle_name', models.CharField(blank=True, default='', max_length=60)),
            ],
            options={
                'ordering': ('family_name', 'given_name', 'middle_name'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_name', models.CharField(default='', max_length=60)),
                ('family_name', models.CharField(default='', max_length=60)),
                ('middle_name', models.CharField(blank=True, default='', max_length=60)),
                ('designation', models.CharField(max_length=60)),
                ('suffix', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('family_name', 'given_name', 'middle_name'),
                'abstract': False,
            },
        ),
    ]
