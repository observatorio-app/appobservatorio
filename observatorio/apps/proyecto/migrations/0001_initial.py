# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-09 19:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnoPublicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_publicacion', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Asesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_asesor', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='inicioModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_inicio', models.CharField(max_length=100)),
                ('imagen_presentacion', models.ImageField(blank=True, null=True, upload_to='img/inicio/')),
                ('descripcion_inicio', models.CharField(max_length=2000)),
                ('principal_inicio', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_programa', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proyecto', models.CharField(max_length=300)),
                ('descripcion_proyecto', models.CharField(max_length=1500)),
                ('nombre_autor', models.CharField(max_length=80)),
                ('fecha_subido', models.DateField(auto_now=True)),
                ('codigo_barras', models.CharField(max_length=100)),
                ('codigo_topografico', models.CharField(max_length=100)),
                ('documento', models.FileField(upload_to='file/')),
            ],
        ),
        migrations.CreateModel(
            name='Tematica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tematica', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='TipoSolucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo_solucion', models.CharField(max_length=80)),
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
            name='fecha_publicacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='proyecto.AnoPublicacion'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='programa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proyecto.Programa'),
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
