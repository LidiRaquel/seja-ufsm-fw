from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from SiteSejaUfsm import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^ alimentacao$', views.alimentacao, name='alimentacao'),
	url(r'^ hospedagem$', views.hospedagem, name='hospedagem'),
	url(r'^ moradia$', views.moradia, name='moradia'),
	url(r'^ contatos$', views.contatos, name='contatos'),
	url(r'^ assistencia$', views.assistencia, name='assistencia'),
	url(r'^ horario$', views.horario, name='horario'),
	url(r'^ index/(?P<id>[0-9]+)/DetalheCursos$', views.DetalheCursos, name='DetalheCursos'),
	url(r'^ agronomia$', views.agronomia, name='agronomia'),
	url(r'^ engenharia_ambiental$', views.engenharia_ambiental, name='engenharia_ambiental'),
	url(r'^ jornalismo$', views.jornalismo, name='jornalismo'),
	url(r'^ engenharia_florestal$', views.engenharia_florestal, name='engenharia_florestal'),
	url(r'^ relacoes_publicas$', views.relacoes_publicas, name='relacoes_publicas'),
	url(r'^ sistemas_informacao$', views.sistemas_informacao, name='sistemas_informacao'),
	url(r'^ index/(?P<id>[0-9]+)/DetalhesNoticias$', views.DetalhesNoticias, name='DetalhesNoticias'),
	url(r'^ galeria$', views.galeria, name='galeria'),
	url(r'^ edital$', views.edital, name='edital'),
	url(r'^ contatos_oficiais$', views.contatos_oficiais, name='contatos_oficiais'),

	#url(r'^ index/(?P<id>[0-9]+)/Curso$', views.Curso, name='Curso'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
