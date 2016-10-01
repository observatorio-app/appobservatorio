# -*- encoding: utf-8 -*-
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy, reverse
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
		if self.request.GET.get('buscar_por') is not None:
			queryset = queryset.filter(nombre_proyecto__icontains = self.request.GET.get('buscar_por'))
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

class ProyectoDetailView(DetailView):
	model = Proyecto
	template_name = template_dir+'detalle_proyecto.html'

	def get_context_data(self, **kwargs):
		context = super(ProyectoDetailView, self).get_context_data(**kwargs)
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

class ProyectoCreateView(SuccessMessageMixin, CreateView):
	template_name = template_dir+'form_proyecto.html'
	success_message = 'Proyecto agregado correctamente'
	form_class = ProjectForm

	def get_context_data(self, **kwargs):
		context = super(ProyectoCreateView, self).get_context_data(**kwargs)
		context['title'] = 'Agregar proyecto'
		context['url'] = '/proyecto/crear/'
		return context

	def form_valid(self, form):
		form.instance.usuario = self.request.user
		form.save()
		return super(ProyectoCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse('detalle_proyecto',args=(self.object.id,))

class ProyectoUpdateView(SuccessMessageMixin, UpdateView):
	model = Proyecto
	template_name = template_dir+'form_proyecto.html'
	success_message = 'Proyecto actualizado correctamente'
	form_class = ProjectForm

	def get_context_data(self, **kwargs):
		context = super(ProyectoUpdateView, self).get_context_data(**kwargs)
		context['title'] = 'Actualizar proyecto'
		context['url'] = '/proyecto/'+self.kwargs['pk']+'/actualizar/'
		return context

	def form_valid(self, form):
		form.instance.usuario = self.request.user
		form.save()
		return super(ProyectoUpdateView, self).form_valid(form)

	def get_success_url(self):
		return reverse('detalle_proyecto',args=(self.object.id,))

class ProyectoDeleteView(DeleteView):
	model = Proyecto
	template_name = template_dir+'delete_proyecto.html'

	def get_context_data(self, **kwargs):
		context = super(ProyectoDeleteView, self).get_context_data(**kwargs)
		context['title'] = 'Confirmación'
		return context

	def get_success_url(self):
		return reverse('inicio')

class AsesorCreateView(SuccessMessageMixin, CreateView):
	template_name = template_dir+'form_general.html'
	success_message = 'Asesor agregado correctamente'
	form_class = AsesorForm

	def get_context_data(self, **kwargs):
		context = super(AsesorCreateView, self).get_context_data(**kwargs)
		context['title'] = 'Agregar asesor'
		context['url'] = '/asesor/crear/'
		return context

	def get_success_url(self):
		return reverse('lista_asesor')

class AsesorUpdateView(SuccessMessageMixin, UpdateView):
	model = Asesor
	template_name = template_dir+'form_general.html'
	success_message = 'Asesor actualizado correctamente'
	form_class = AsesorForm

	def get_context_data(self, **kwargs):
		context = super(AsesorUpdateView, self).get_context_data(**kwargs)
		context['title'] = 'Actualizar asesor'
		context['url'] = '/asesor/'+self.kwargs['pk']+'/actualizar/'
		return context

	def get_success_url(self):
		return reverse('lista_asesor')

class AsesorDeleteView(DeleteView):
	model = Asesor
	template_name = template_dir+'delete_asesor.html'

	def get_context_data(self, **kwargs):
		context = super(AsesorDeleteView, self).get_context_data(**kwargs)
		context['title'] = 'Confirmación'
		return context

	def get_success_url(self):
		return reverse('lista_asesor')

class TematicaListView(ListView):
	model = Tematica
	paginate_by = 10
	form_class = TematicaForm
	template_name = template_dir+'lista_tematica.html'

	def get_context_data(self, **kwargs):
		context = super(TematicaListView, self).get_context_data(**kwargs)
		context['title'] = 'Listado de temáticas'
		return context

class TematicaCreateView(SuccessMessageMixin, CreateView):
	template_name = template_dir+'form_general.html'
	success_message = 'Temática agregada correctamente'
	form_class = TematicaForm

	def get_context_data(self, **kwargs):
		context = super(TematicaCreateView, self).get_context_data(**kwargs)
		context['title'] = 'Agregar temática'
		context['url'] = '/tematicas/crear/'
		return context

	def get_success_url(self):
		return reverse('lista_tematica')

class TematicaUpdateView(SuccessMessageMixin, UpdateView):
	model = Tematica
	template_name = template_dir+'form_general.html'
	success_message = 'Temática actualizada correctamente'
	form_class = TematicaForm

	def get_context_data(self, **kwargs):
		context = super(TematicaUpdateView, self).get_context_data(**kwargs)
		context['title'] = 'Actualizar temática'
		context['url'] = '/tematicas/'+self.kwargs['pk']+'/actualizar/'
		return context

	def get_success_url(self):
		return reverse('lista_tematica')

class TematicaDeleteView(DeleteView):
	model = Tematica
	template_name = template_dir+'delete_tematica.html'

	def get_context_data(self, **kwargs):
		context = super(TematicaDeleteView, self).get_context_data(**kwargs)
		context['title'] = 'Confirmación'
		return context

	def get_success_url(self):
		return reverse('lista_tematica')

class SolucionListView(ListView):
	model = TipoSolucion
	paginate_by = 10
	form_class = SolucionForm
	template_name = template_dir+'lista_solucion.html'

	def get_context_data(self, **kwargs):
		context = super(SolucionListView, self).get_context_data(**kwargs)
		context['title'] = 'Listado de tipo de soluciones'
		return context

class SolucionCreateView(SuccessMessageMixin, CreateView):
	template_name = template_dir+'form_general.html'
	success_message = 'Tipo de solución agregado correctamente'
	form_class = SolucionForm

	def get_context_data(self, **kwargs):
		context = super(SolucionCreateView, self).get_context_data(**kwargs)
		context['title'] = 'Agregar tipo de solución'
		context['url'] = '/solucion/crear/'
		return context

	def get_success_url(self):
		return reverse('lista_solucion')

class SolucionUpdateView(SuccessMessageMixin, UpdateView):
	model = TipoSolucion
	template_name = template_dir+'form_general.html'
	success_message = 'Tipo de solución actualizada correctamente'
	form_class = SolucionForm

	def get_context_data(self, **kwargs):
		context = super(SolucionUpdateView, self).get_context_data(**kwargs)
		context['title'] = 'Actualizar tipo de solución'
		context['url'] = '/solucion/'+self.kwargs['pk']+'/actualizar/'
		return context

	def get_success_url(self):
		return reverse('lista_solucion')

class SolucionDeleteView(DeleteView):
	model = TipoSolucion
	template_name = template_dir+'delete_solucion.html'

	def get_context_data(self, **kwargs):
		context = super(SolucionDeleteView, self).get_context_data(**kwargs)
		context['title'] = 'Confirmación'
		return context

	def get_success_url(self):
		return reverse('lista_solucion')

class AnoPublicacionListView(ListView):
	model = AnoPublicacion
	paginate_by = 10
	form_class = AnoPublicacionForm
	template_name = template_dir+'lista_ano_publicacion.html'

	def get_context_data(self, **kwargs):
		context = super(AnoPublicacionListView, self).get_context_data(**kwargs)
		context['title'] = 'Listado de año de publicación'
		return context

class AnoPublicacionCreateView(SuccessMessageMixin, CreateView):
	template_name = template_dir+'form_general.html'
	success_message = 'Año de publicación agregado correctamente'
	form_class = AnoPublicacionForm

	def get_context_data(self, **kwargs):
		context = super(AnoPublicacionCreateView, self).get_context_data(**kwargs)
		context['title'] = 'Agregar año de publicación'
		context['url'] = '/ano-publicacion/crear/'
		return context

	def get_success_url(self):
		return reverse('lista_ano_publicacion')

class AnoPublicacionUpdateView(SuccessMessageMixin, UpdateView):
	model = AnoPublicacion
	template_name = template_dir+'form_general.html'
	success_message = 'Año de publicación actualizada correctamente'
	form_class = AnoPublicacionForm

	def get_context_data(self, **kwargs):
		context = super(AnoPublicacionUpdateView, self).get_context_data(**kwargs)
		context['title'] = 'Actualizar año de publicación'
		context['url'] = '/ano-publicacion/'+self.kwargs['pk']+'/actualizar/'
		return context

	def get_success_url(self):
		return reverse('lista_ano_publicacion')

class AnoPublicacionDeleteView(DeleteView):
	model = AnoPublicacion
	template_name = template_dir+'delete_ano_publicacion.html'

	def get_context_data(self, **kwargs):
		context = super(AnoPublicacionDeleteView, self).get_context_data(**kwargs)
		context['title'] = 'Confirmación'
		return context

	def get_success_url(self):
		return reverse('lista_ano_publicacion')