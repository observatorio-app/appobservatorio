# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-09 20:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0005_proyecto_tipo_tematica'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyecto',
            old_name='tipo_tematica',
            new_name='area_tematica',
        ),
    ]