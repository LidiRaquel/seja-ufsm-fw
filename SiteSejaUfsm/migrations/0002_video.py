# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-15 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteSejaUfsm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('URL', models.URLField(blank=True, max_length=300)),
            ],
        ),
    ]
