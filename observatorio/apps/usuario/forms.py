# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django.forms import *
from django import forms

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'is_superuser')
		widgets = {
			'username': TextInput(attrs = {'class': 'form-control', 'maxlength': '15', 'required': True}),
			'first_name': TextInput(attrs = {'class': 'form-control', 'maxlength': '30', 'required': True}),
			'last_name': TextInput(attrs = {'class': 'form-control', 'maxlength': '30', 'required': True}),
			'email': EmailInput(attrs = {'class': 'form-control', 'maxlength': '30', 'required': True}),
		}
		labels = {
			'username': 'Nombre de usuario',
			'first_name': 'Nombres',
			'last_name': 'Apellidos',
			'email': 'Correo electrónico',
			'is_superuser': 'Administrador',
		}