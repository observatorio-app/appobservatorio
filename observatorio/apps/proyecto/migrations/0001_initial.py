# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-10 20:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_asesor', models.CharField(max_length=45)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proyecto', models.CharField(max_length=150)),
                ('descripcion_proyecto', models.CharField(max_length=120)),
                ('nombre_autor', models.CharField(max_length=80)),
                ('fecha_publicacion', models.CharField(max_length=4)),
                ('fecha_subido', models.DateField()),
                ('codigo_barras', models.CharField(max_length=20)),
                ('codigo_topografico', models.CharField(max_length=20)),
                ('documento', models.FileField(upload_to='file/')),
            ],
        ),
        migrations.CreateModel(
            name='Tematica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tematica', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='TipoSolucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo_solucion', models.CharField(max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='proyecto',
            name='area_tematica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Tematica'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='asesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.Asesor'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='tipo_solucion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.TipoSolucion'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
