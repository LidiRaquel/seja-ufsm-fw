# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-20 12:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SiteSejaUfsm', '0002_auto_20171220_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contato_administrativo',
            name='Setor',
        ),
    ]
