from django.conf.urls import patterns, url, include
from .views import *

project_patterns = [
	url(r'^$', ProyectoDetaiView.as_view(), name='detalle_proyecto'),
	url(r'^descargar/$', download_document, name = 'download_document'),
]

urlpatterns = patterns('observatorio.apps.proyecto.views',
	url(r'^$', ProyectoListView.as_view(), name = 'inicio'),
	url(r'^proyecto/(?P<pk>[0-9]+)/', include(project_patterns)),
)