# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('birth_date', models.DateField()),
                ('image_url', models.URLField()),
                ('score', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]
