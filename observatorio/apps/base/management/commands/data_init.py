# -*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand
from observatorio.apps.base.models import Estado
from observatorio.apps.proyecto.models import *

class Command(BaseCommand):

	def handle(self, *args, **options):
		TipoSolucion.objects.all().delete()
		Asesor.objects.all().delete()
		Tematica.objects.all().delete()
		Proyecto.objects.all().delete()
		Estado.objects.all().delete()
		AnoPublicacion.objects.all().delete()
		print "Datos Eliminados"
		TipoSolucion.objects.create(nombre_tipo_solucion = "Software Educativo")
		TipoSolucion.objects.create(nombre_tipo_solucion = "Recurso Educativo")
		TipoSolucion.objects.create(nombre_tipo_solucion = "Software Diagnóstico")
		TipoSolucion.objects.create(nombre_tipo_solucion = "Sistema Administración Remota")
		TipoSolucion.objects.create(nombre_tipo_solucion = "Bodega de Datos")
		TipoSolucion.objects.create(nombre_tipo_solucion = "Análisis y Diseño de Redes")
		TipoSolucion.objects.create(nombre_tipo_solucion = "Aplicación Web/Móvil")
		TipoSolucion.objects.create(nombre_tipo_solucion = "Help Desk")
		TipoSolucion.objects.create(nombre_tipo_solucion = "Investigación")
		TipoSolucion.objects.create(nombre_tipo_solucion = "Módulo Adicional")
		TipoSolucion.objects.create(nombre_tipo_solucion = "Simulador")
		print "Tipo de Solución creados"
		Tematica.objects.create(nombre_tematica = "Software")
		Tematica.objects.create(nombre_tematica = "Hardware")
		Tematica.objects.create(nombre_tematica = "Redes y Telecomunicaciones")
		Tematica.objects.create(nombre_tematica = "Bodegas de Datos")
		Tematica.objects.create(nombre_tematica = "Bases de Datos")
		print "Temática creados"
		activo = Estado.objects.create(nombre_estado = "Activo")
		Estado.objects.create(nombre_estado = "Inactivo")
		print "Estados creados"
		Asesor.objects.create(nombre_asesor = "Elkin Oswaldo Forero Soto", estado = activo)
		Asesor.objects.create(nombre_asesor = "Ludwig Iván Trujillo Hernandez", estado = activo)
		Asesor.objects.create(nombre_asesor = "Luis Fernando Cetares Ruiz", estado = activo)
		Asesor.objects.create(nombre_asesor = "Ninguno", estado = activo)
		Asesor.objects.create(nombre_asesor = "Jinneth Tique Ortiz", estado = activo)
		print "Asesores creados"
		AnoPublicacion.objects.create(pk = 1991, fecha_publicacion = "1991")
		AnoPublicacion.objects.create(pk = 1992, fecha_publicacion = "1992")
		AnoPublicacion.objects.create(pk = 1993, fecha_publicacion = "1993")
		AnoPublicacion.objects.create(pk = 1994, fecha_publicacion = "1994")
		AnoPublicacion.objects.create(pk = 1995, fecha_publicacion = "1995")
		AnoPublicacion.objects.create(pk = 1996, fecha_publicacion = "1996")
		AnoPublicacion.objects.create(pk = 1997, fecha_publicacion = "1997")
		AnoPublicacion.objects.create(pk = 1998, fecha_publicacion = "1998")
		AnoPublicacion.objects.create(pk = 1999, fecha_publicacion = "1999")
		AnoPublicacion.objects.create(pk = 2001, fecha_publicacion = "2001")
		AnoPublicacion.objects.create(pk = 2002, fecha_publicacion = "2002")
		AnoPublicacion.objects.create(pk = 2003, fecha_publicacion = "2003")
		AnoPublicacion.objects.create(pk = 2004, fecha_publicacion = "2004")
		AnoPublicacion.objects.create(pk = 2005, fecha_publicacion = "2005")
		AnoPublicacion.objects.create(pk = 2006, fecha_publicacion = "2006")
		AnoPublicacion.objects.create(pk = 2007, fecha_publicacion = "2007")
		AnoPublicacion.objects.create(pk = 2008, fecha_publicacion = "2008")
		AnoPublicacion.objects.create(pk = 2009, fecha_publicacion = "2009")
		AnoPublicacion.objects.create(pk = 2010, fecha_publicacion = "2010")
		AnoPublicacion.objects.create(pk = 2011, fecha_publicacion = "2011")
		AnoPublicacion.objects.create(pk = 2012, fecha_publicacion = "2012")
		AnoPublicacion.objects.create(pk = 2013, fecha_publicacion = "2013")
		AnoPublicacion.objects.create(pk = 2014, fecha_publicacion = "2014")
		AnoPublicacion.objects.create(pk = 2015, fecha_publicacion = "2015")
		print "Años creados"