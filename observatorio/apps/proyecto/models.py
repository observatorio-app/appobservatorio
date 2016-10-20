from __future__ import unicode_literals

# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

class inicioModel(models.Model):
	titulo_inicio = models.CharField(max_length = 100)
	descripcion_inicio = models.CharField(max_length = 2000)
	imagen = models.ImageField(upload_to = 'img/', blank = True, null = True)

	def __str__(self):
		return self.titulo_inicio

	def __unicode__(self):
		return self.titulo_inicio

class TipoSolucion(models.Model):
	nombre_tipo_solucion = models.CharField(max_length = 80)

	def __str__(self):
		return self.nombre_tipo_solucion

	def __unicode__(self):
		return self.nombre_tipo_solucion

class Asesor(models.Model):
	nombre_asesor = models.CharField(max_length = 80)

	def __str__(self):
		return self.nombre_asesor

	def __unicode__(self):
		return self.nombre_asesor

class Tematica(models.Model):
	nombre_tematica = models.CharField(max_length = 80)

	def __str__(self):
		return self.nombre_tematica

	def __unicode__(self):
		return self.nombre_tematica

class AnoPublicacion(models.Model):
	fecha_publicacion = models.CharField(max_length = 7)

	def __str__(self):
		return self.fecha_publicacion

	def __unicode__(self):
		return self.fecha_publicacion

class Programa(models.Model):
	nombre_programa = models.CharField(max_length = 150)

	def __str__(self):
		return self.nombre_programa

	def __unicode__(self):
		return self.nombre_programa

class Proyecto(models.Model):
	nombre_proyecto = models.CharField(max_length = 300)
	descripcion_proyecto = models.CharField(max_length = 1500)
	nombre_autor = models.CharField(max_length = 80)
	asesor = models.ForeignKey(Asesor)
	tipo_solucion = models.ForeignKey(TipoSolucion)
	area_tematica = models.ForeignKey(Tematica)
	fecha_publicacion = models.ForeignKey(AnoPublicacion, default = 1)
	fecha_subido = models.DateField(auto_now = True)
	codigo_barras = models.CharField(max_length = 100)
	codigo_topografico = models.CharField(max_length = 100)
	documento = models.FileField(upload_to = 'file/')
	usuario = models.ForeignKey(User)
	programa = models.ForeignKey(Programa, default = 1)

	def __str__(self):
		return self.nombre_proyecto

	def __unicode__(self):
		return self.nombre_proyecto