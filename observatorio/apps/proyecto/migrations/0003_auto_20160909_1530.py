# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-09 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0002_auto_20160909_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_publicacion',
            field=models.IntegerField(),
        ),
    ]