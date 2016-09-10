# -*- encoding: utf-8 -*-
from observatorio.apps.proyecto.models import Proyecto
from django import template
import datetime

register = template.Library()

@register.simple_tag()
def date_now():
	return datetime.datetime.now().date().strftime("%A, %d de %B del %Y")

@register.assignment_tag
def relation_project(pk):
	proyecto = Proyecto.objects.get(pk = pk)
	area_tematica = proyecto.area_tematica.proyecto_set.exclude(pk = proyecto.pk)
	tipo_solucion = proyecto.tipo_solucion.proyecto_set.exclude(pk = proyecto.pk)
	usuario = proyecto.usuario.proyecto_set.exclude(pk = proyecto.pk)
	asesor = proyecto.asesor.proyecto_set.exclude(pk = proyecto.pk)
	return area_tematica[:3] if area_tematica.count() > 0 else tipo_solucion[:3] if tipo_solucion.count() > 0 else asesor[:3] if asesor.count() > 0 else usuario[:3]