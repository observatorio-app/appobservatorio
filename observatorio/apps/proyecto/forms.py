# -*- encoding: utf-8 -*-
from django.forms import *
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

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Proyecto
		fields = '__all__'
		exclude = ('usuario',)
		widgets = {
			'nombre_proyecto': TextInput(attrs = {'class': 'form-control', 'maxlength': '150', 'required': True}),
			'descripcion_proyecto': Textarea(attrs = {'rows': 5, 'class': 'form-control', 'maxlength': '1000', 'required': True}),
			'nombre_autor': TextInput(attrs = {'class': 'form-control', 'maxlength': '80', 'required': True}),
			'codigo_barras': TextInput(attrs = {'class': 'form-control', 'maxlength': '20', 'required': True}),
			'codigo_topografico': TextInput(attrs = {'class': 'form-control', 'maxlength': '20', 'required': True}),
		}
		labels = {
			'nombre_proyecto': 'Nombre del proyecto',
			'descripcion_proyecto': 'Descripción del proyecto',
			'nombre_autor': 'Nombre del autor',
			'asesor': 'Asesor del proyecto',
			'tipo_solucion': 'Tipo de solución',
			'area_tematica': 'Temática del proyecto',
			'fecha_publicacion': 'Año de publicación',
			'codigo_barras': 'Código de barras',
			'codigo_topografico': 'Código topográfico',
			'documento': 'Subir proyecto',
		}

	def __init__(self, *args, **kwargs):
		super(ProjectForm, self).__init__(*args, **kwargs)
		self.fields['asesor'].widget.attrs.update({'required': True, 'class': 'form-control'})
		self.fields['tipo_solucion'].widget.attrs.update({'required': True, 'class': 'form-control'})
		self.fields['area_tematica'].widget.attrs.update({'required': True, 'class': 'form-control'})
		self.fields['fecha_publicacion'].widget.attrs.update({'required': True, 'class': 'form-control'})

class AsesorForm(forms.ModelForm):
	class Meta:
		model = Asesor
		fields = '__all__'
		widgets = {
			'nombre_asesor': TextInput(attrs = {'class': 'form-control', 'maxlength': '45', 'required': True}),
		}
		labels = {
			'nombre_asesor': 'Nombre del asesor',
		}

class TematicaForm(forms.ModelForm):
	class Meta:
		model = Tematica
		fields = '__all__'
		widgets = {
			'nombre_tematica': TextInput(attrs = {'class': 'form-control', 'maxlength': '45', 'required': True}),
		}
		labels = {
			'nombre_tematica': 'Nombre de la temática',
		}

class SolucionForm(forms.ModelForm):
	class Meta:
		model = TipoSolucion
		fields = '__all__'
		widgets = {
			'nombre_tipo_solucion': TextInput(attrs = {'class': 'form-control', 'maxlength': '45', 'required': True}),
		}
		labels = {
			'nombre_tipo_solucion': 'Nombre del tipo de solución',
		}

class AnoPublicacionForm(forms.ModelForm):
	class Meta:
		model = AnoPublicacion
		fields = '__all__'
		widgets = {
			'fecha_publicacion': TextInput(attrs = {'class': 'form-control', 'maxlength': '7', 'required': True}),
		}
		labels = {
			'fecha_publicacion': 'Digíte el año',
		}