# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-15 13:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SiteSejaUfsm', '0005_auto_20171215_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='Imagem_2',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='Imagem_3',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='Imagem_4',
        ),
    ]
