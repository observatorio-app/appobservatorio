from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from .views import *

project_detail_patterns = [
	url(r'^$', ProyectoDetailView.as_view(), name='detalle_proyecto'),
	url(r'^actualizar/$', login_required(ProyectoUpdateView.as_view()), name='edit_proyecto'),
	url(r'^eliminar/$', login_required(ProyectoDeleteView.as_view()), name='delete_proyecto'),
	url(r'^descargar/$', download_document, name = 'download_document'),
]

asesor_detail_patterns = [
	url(r'^actualizar/$', login_required(AsesorUpdateView.as_view()), name='edit_asesor'),
	url(r'^eliminar/$', login_required(AsesorDeleteView.as_view()), name='delete_asesor'),
]

tematica_detail_patterns = [
	url(r'^actualizar/$', login_required(TematicaUpdateView.as_view()), name='edit_tematica'),
	url(r'^eliminar/$', login_required(TematicaDeleteView.as_view()), name='delete_tematica'),
]

solucion_detail_patterns = [
	url(r'^actualizar/$', login_required(SolucionUpdateView.as_view()), name='edit_solucion'),
	url(r'^eliminar/$', login_required(SolucionDeleteView.as_view()), name='delete_solucion'),
]

ano_publicacion_detail_patterns = [
	url(r'^actualizar/$', login_required(AnoPublicacionUpdateView.as_view()), name='edit_ano_publicacion'),
	url(r'^eliminar/$', login_required(AnoPublicacionDeleteView.as_view()), name='delete_ano_publicacion'),
]

project_patterns = [
	url(r'^(?P<pk>\d+)/', include(project_detail_patterns)),
	url(r'^crear/$', login_required(ProyectoCreateView.as_view()), name='crear_proyecto'),
]

asesor_patterns = [
	url(r'^$', AsesorListView.as_view(), name = 'lista_asesor'),
	url(r'^(?P<pk>\d+)/', include(asesor_detail_patterns)),
	url(r'^crear/$', login_required(AsesorCreateView.as_view()), name='crear_asesor'),
]

tematicas_patterns = [
	url(r'^$', TematicaListView.as_view(), name = 'lista_tematica'),
	url(r'^(?P<pk>\d+)/', include(tematica_detail_patterns)),
	url(r'^crear/$', login_required(TematicaCreateView.as_view()), name='crear_tematica'),
]

solucion_patterns = [
	url(r'^$', SolucionListView.as_view(), name = 'lista_solucion'),
	url(r'^(?P<pk>\d+)/', include(solucion_detail_patterns)),
	url(r'^crear/$', login_required(SolucionCreateView.as_view()), name='crear_solucion'),
]

ano_publicacion_patterns = [
	url(r'^$', AnoPublicacionListView.as_view(), name = 'lista_ano_publicacion'),
	url(r'^(?P<pk>\d+)/', include(ano_publicacion_detail_patterns)),
	url(r'^crear/$', login_required(AnoPublicacionCreateView.as_view()), name='crear_ano_publicacion'),
]

urlpatterns = patterns('observatorio.apps.proyecto.views',
	url(r'^$', ProyectoListView.as_view(), name = 'inicio'),
	url(r'^proyecto/', include(project_patterns)),
	url(r'^asesor/', include(asesor_patterns)),
	url(r'^tematicas/', include(tematicas_patterns)),
	url(r'^solucion/', include(solucion_patterns)),
	url(r'^ano-publicacion/', include(ano_publicacion_patterns)),
	url(r'^quienes-somos/$', TemplateView.as_view(template_name = 'proyecto/quienes-somos.html'), name = 'quienes_somos'),
)