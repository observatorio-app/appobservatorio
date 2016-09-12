# -*- encoding: utf-8 -*-
from django import forms
from .models import *

class ProyectoSearchForm(forms.Form):
	ordenar_por = forms.ChoiceField(choices = [('', 'Seleccione una opción'), ('1', 'Fecha ascendente'), ('2', 'Fecha descendente'), ('3', 'Título ascendente'), ('4', 'Título descendente')], label = 'Ordenar por:', widget = forms.Select(attrs = {'class': 'form-control'}))
	filtro_solucion = forms.MultipleChoiceField(label = 'Filtrar por tipo de solución:', widget = forms.CheckboxSelectMultiple())
	filtro_tematica = forms.MultipleChoiceField(label = 'Filtrar por tipo temática:', widget = forms.CheckboxSelectMultiple())
	filtro_anio = forms.MultipleChoiceField(label = 'Filtrar por año:', widget = forms.CheckboxSelectMultiple())

	def __init__(self, *args, **kwargs):
		ordenar_por = kwargs.pop('ordenar_por', None)
		filtro_solucion = kwargs.pop('filtro_solucion', None)
		filtro_tematica = kwargs.pop('filtro_tematica', None)
		filtro_anio = kwargs.pop('filtro_anio', None)
		super(ProyectoSearchForm, self).__init__(*args, **kwargs)
		self.fields['filtro_solucion'].choices = [(x.pk, x.nombre_tipo_solucion) for x in TipoSolucion.objects.all()]
		self.fields['filtro_tematica'].choices = [(x.pk, x.nombre_tematica) for x in Tematica.objects.all()]
		self.fields['filtro_anio'].choices = [(x.pk, x.fecha_publicacion) for x in AnoPublicacion.objects.all()]
		if ordenar_por: self.fields['ordenar_por'].initial = ordenar_por
		if filtro_solucion: self.fields['filtro_solucion'].initial = filtro_solucion
		if filtro_tematica: self.fields['filtro_tematica'].initial = filtro_tematica
		if filtro_anio: self.fields['filtro_anio'].initial = filtro_anio