# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-18 13:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alimentacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(blank=True, max_length=100)),
                ('Endereco', models.CharField(blank=True, max_length=100, verbose_name='Endereço')),
                ('Telefone', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(blank=True, max_length=100)),
                ('Telefone', models.CharField(blank=True, max_length=100)),
                ('Email', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contato_Administrativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(blank=True, max_length=100)),
                ('Setor', models.CharField(blank=True, max_length=100)),
                ('Telefone', models.CharField(blank=True, max_length=100)),
                ('Email', models.CharField(blank=True, max_length=100)),
                ('Site', models.URLField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Logo', models.ImageField(blank=True, null=True, upload_to='logos')),
                ('Nome', models.CharField(blank=True, max_length=100)),
                ('Vagas', models.CharField(blank=True, max_length=100)),
                ('Duracao', models.CharField(blank=True, max_length=100, verbose_name='Duração')),
                ('Turno', models.CharField(blank=True, max_length=100)),
                ('Objetivo', models.TextField(blank=True)),
                ('Perfil', models.TextField(blank=True)),
                ('Atuacao', models.TextField(blank=True, verbose_name='Atuação')),
                ('Coordenador', models.CharField(blank=True, max_length=100)),
                ('Telefone', models.CharField(blank=True, max_length=100)),
                ('Email', models.EmailField(blank=True, max_length=100)),
                ('Grade', models.URLField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Edital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data', models.DateField(blank=True)),
                ('Nome', models.CharField(blank=True, max_length=100)),
                ('Arquivo', models.FileField(blank=True, upload_to='media/arquivos')),
            ],
        ),
        migrations.CreateModel(
            name='Hotei',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(blank=True, max_length=100)),
                ('Endereco', models.CharField(blank=True, max_length=100, verbose_name='Endereço')),
                ('Telefone', models.CharField(blank=True, max_length=100)),
                ('Site', models.URLField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(blank=True, max_length=100)),
                ('Imagem', models.ImageField(blank=True, null=True, upload_to='galeria')),
                ('idcurso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SiteSejaUfsm.Curso', verbose_name='Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Imobiliaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(blank=True, max_length=100)),
                ('Endereco', models.CharField(blank=True, max_length=100, verbose_name='Endereço')),
                ('Telefone', models.CharField(blank=True, max_length=100)),
                ('Site', models.URLField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(blank=True, max_length=100)),
                ('Data', models.DateField(blank=True)),
                ('Descricao', models.CharField(blank=True, max_length=150, verbose_name='Descrição')),
                ('Texto', models.TextField(blank=True)),
                ('idcurso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SiteSejaUfsm.Curso', verbose_name='Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(blank=True, max_length=100)),
                ('URL', models.CharField(blank=True, max_length=300, verbose_name='Vídeo')),
                ('idcurso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SiteSejaUfsm.Curso', verbose_name='Curso')),
            ],
        ),
        migrations.AddField(
            model_name='imagen',
            name='idnoticia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SiteSejaUfsm.Noticia', verbose_name='Notícia'),
        ),
    ]
