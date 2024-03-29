# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-01 04:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('H_id', models.IntegerField()),
                ('D_name', models.CharField(max_length=50)),
                ('specialist', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=11)),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('H_id', models.IntegerField()),
                ('H_name', models.CharField(max_length=50)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('mobile', models.CharField(max_length=11)),
                ('H_address', models.CharField(max_length=250)),
            ],
        ),
    ]
