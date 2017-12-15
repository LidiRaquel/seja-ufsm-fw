# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-15 14:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SiteSejaUfsm', '0006_auto_20171215_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='Imagem',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='Noticia',
        ),
        migrations.AddField(
            model_name='imagen',
            name='idcurso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SiteSejaUfsm.Curso', verbose_name='Curso'),
        ),
        migrations.AddField(
            model_name='noticia',
            name='idcurso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SiteSejaUfsm.Curso', verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='alimentacao',
            name='Endereco',
            field=models.CharField(blank=True, max_length=100, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='Atuacao',
            field=models.TextField(blank=True, verbose_name='Atuação'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='Duracao',
            field=models.CharField(blank=True, max_length=100, verbose_name='Duração'),
        ),
        migrations.AlterField(
            model_name='hotei',
            name='Endereco',
            field=models.CharField(blank=True, max_length=100, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='imobiliaria',
            name='Endereco',
            field=models.CharField(blank=True, max_length=100, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='Data',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='Descricao',
            field=models.CharField(blank=True, max_length=150, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='video',
            name='URL',
            field=models.URLField(blank=True, max_length=300, verbose_name='URL para compartilhar'),
        ),
    ]
