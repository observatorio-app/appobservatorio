from django.contrib.auth.decorators import user_passes_test, permission_required
from django.conf.urls import patterns, url, include
from django.contrib.auth import views as auth_views
from .views import *

login_forbidden = user_passes_test(lambda u: u.is_anonymous(), '/')

urlpatterns = patterns('observatorio.apps.usuario.views',
	url(r'^(?P<pk>\d+)/actualizar/$', permission_required('is_superuser')(UserUpdateView.as_view()), name = 'update_user'),
	url(r'^crear/$', permission_required('is_superuser')(UserCreateView.as_view()), name = 'new_user'),
	url(r'^lista/$', permission_required('is_superuser')(UserListView.as_view()), name = 'list_user'),
	url(r'^ingresar/$', login_forbidden(auth_views.login), {'template_name': 'usuario/form_login.html', 'extra_context': {'title': 'Ingresar'}}, name = 'login'),
	url(r'^salir/$', auth_views.logout, {'next_page': '/'}, name = 'logout')
)