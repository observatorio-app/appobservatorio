# -*- encoding: utf-8 -*-
from django.views.generic import ListView, DetailView
from observatorio.apps.proyecto.models import *
from django.views.generic.edit import FormMixin
from django.shortcuts import render, redirect
from .forms import *

template_dir = 'proyecto/'

class ProyectoListView(FormMixin, ListView):
	model = Proyecto
	paginate_by = 10
	form_class = ProyectoSearchForm
	template_name = template_dir+'lista_proyecto.html'

	def get_context_data(self, **kwargs):
		context = super(ProyectoListView, self).get_context_data(**kwargs)
		context['title'] = 'Listado de proyectos'
		return context

	def get_form_kwargs(self):
		kwargs = super(ProyectoListView, self).get_form_kwargs()
		kwargs['ordenar_por'] = self.request.GET.get('ordenar_por')
		kwargs['filtro_solucion'] = self.request.GET.getlist('filtro_solucion')
		kwargs['filtro_tematica'] = self.request.GET.getlist('filtro_tematica')
		kwargs['filtro_anio'] = self.request.GET.getlist('filtro_anio')
		return kwargs

	def get_queryset(self):
		queryset = super(ProyectoListView, self).get_queryset()
		if self.request.GET.get('ordenar_por') == '1':
			queryset = queryset.order_by('fecha_publicacion')
		if self.request.GET.get('ordenar_por') == '2':
			queryset = queryset.order_by('-fecha_publicacion')
		if self.request.GET.get('ordenar_por') == '3':
			queryset = queryset.order_by('nombre_proyecto')
		if self.request.GET.get('ordenar_por') == '4':
			queryset = queryset.order_by('-nombre_proyecto')
		if self.request.GET.getlist('filtro_solucion'): 
			queryset = queryset.filter(tipo_solucion__id__in = self.request.GET.getlist('filtro_solucion'))
		if self.request.GET.getlist('filtro_tematica'): 
			queryset = queryset.filter(area_tematica__id__in = self.request.GET.getlist('filtro_tematica'))
		if self.request.GET.getlist('filtro_anio'): 
			queryset = queryset.filter(fecha_publicacion__id__in = self.request.GET.getlist('filtro_anio'))
		return queryset

class ProyectoDetaiView(DetailView):
	model = Proyecto
	template_name = template_dir+'detalle_proyecto.html'

	def get_context_data(self, **kwargs):
		context = super(ProyectoDetaiView, self).get_context_data(**kwargs)
		context['title'] = 'Detalle del proyecto'
		return context

class AsesorListView(ListView):
	model = Asesor
	paginate_by = 20
	template_name = template_dir+'lista_asesor.html'

	def get_context_data(self, **kwargs):
		context = super(AsesorListView, self).get_context_data(**kwargs)
		context['title'] = 'Listado de asesores'
		return context

def download_document(request, pk):
	proyecto = Proyecto.objects.get(pk = pk)
	return redirect('%s/%s'%('/static', proyecto.documento))