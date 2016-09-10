# -*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand
from observatorio.apps.base.models import Estado
from observatorio.apps.proyecto.models import *

class Command(BaseCommand):

	def handle(self, *args, **options):
		TipoSolucion.objects.all().delete()
		Asesor.objects.all().delete()
		Tematica.objects.all().delete()
		AutorProyecto.objects.all().delete()
		Proyecto.objects.all().delete()
		Estado.objects.all().delete()
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