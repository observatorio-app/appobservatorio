from observatorio.apps.proyecto.models import Proyecto
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect

template_dir = 'proyecto/'

class ProyectoListView(ListView):
	model = Proyecto
	paginate_by = 10
	template_name = template_dir+'lista_proyecto.html'

	def get_context_data(self, **kwargs):
		context = super(ProyectoListView, self).get_context_data(**kwargs)
		context['title'] = 'Listado de proyectos'
		return context

class ProyectoDetaiView(DetailView):
	model = Proyecto
	template_name = template_dir+'detalle_proyecto.html'

	def get_context_data(self, **kwargs):
		context = super(ProyectoDetaiView, self).get_context_data(**kwargs)
		context['title'] = 'Detalle del proyecto'
		return context

def download_document(request, pk):
	proyecto = Proyecto.objects.get(pk = pk)
	return redirect('%s/%s'%('/static', proyecto.documento))