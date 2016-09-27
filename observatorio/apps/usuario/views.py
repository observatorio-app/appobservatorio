from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import *

var_dir_template = 'usuario/'

class UserListView(ListView):
	template_name = var_dir_template+'list_user.html'
	paginate_by = 10
	model = User

	def get_context_data(self, **kwargs):
		context = super(UserListView, self).get_context_data(**kwargs)
		context['title'] = 'Lista de usuarios'
		return context

class UserCreateView(SuccessMessageMixin, CreateView):
	template_name = var_dir_template+'form_user.html'
	success_message = 'Usuario agregado correctamente'
	success_url = reverse_lazy('list_user')
	form_class = UserForm

	def form_valid(self, form):
		obj = form.save(commit = False)
		obj.set_password(obj.email)
		obj.save()
		return super(UserCreateView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(UserCreateView, self).get_context_data(**kwargs)
		context['title'] = 'Agregar usuario'
		context['url'] = '/usuario/crear/'
		return context

class UserUpdateView(SuccessMessageMixin, UpdateView):
	model = User
	template_name = var_dir_template+'form_user.html'
	success_message = 'Usuario actualizado correctamente'
	success_url = reverse_lazy('list_user')
	form_class = UserForm

	def get_context_data(self, **kwargs):
		context = super(UserUpdateView, self).get_context_data(**kwargs)
		context['title'] = 'Actualizar usuario'
		context['url'] = '/usuario/'+self.kwargs['pk']+'/actualizar/'
		return context

	def form_valid(self, form):
		obj = form.save(commit = False)
		obj.set_password(obj.email)
		obj.save()
		return super(UserUpdateView, self).form_valid(form)