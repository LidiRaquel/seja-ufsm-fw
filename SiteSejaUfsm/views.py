from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#importo as classe da model para trabalhar com o que vier do banco de dados
from .models import Curso
from .models import Alimentacao
from .models import Hotei
from .models import Imobiliaria
from .models import Contato_Administrativo
from .models import Contato
from .models import Imagen
from .models import Noticia
from .models import Edital
from .models import Video

def index(request):
	cursos = Curso.objects.all()
	noticias = Noticia.objects.all().order_by("-id")
	paginator = Paginator(noticias,20)
	page = request.GET.get('page')
	try:
		noticias = paginator.page(page)
	except PageNotAnInteger:
		noticias = paginator.page(1)
	except EmptyPage:
		noticias = paginator.page(paginator.num_pages)
	return render(request,'index_seja.html',{'cursos':cursos,'noticias':noticias,'page': page})

def DetalheCursos(request,id):
	cursos = Curso.objects.all()
	curso = Curso.objects.all().filter(id= id)
	imagem = Imagen.objects.all().filter(idcurso=id).order_by('-id')
	noticias = Noticia.objects.all().filter(idcurso=id).order_by('-id')
	videos = Video.objects.all().filter(idcurso=id).order_by('-id')

	paginator_ = Paginator(noticias,6)
	paginator = Paginator(imagem,4)
	paginator1 = Paginator(videos,3)
	page = request.GET.get('page')
	try:
		imagem = paginator.page(page)
	except PageNotAnInteger:
		imagem = paginator.page(1)
	except EmptyPage:
		imagem = paginator.page(paginator.num_pages)

	try: 
		noticias = paginator_.page(page)
	except PageNotAnInteger:
		noticias = paginator_.page(1)
	except EmptyPage:
		noticias = pagi.page(paginator_.num_pages)

	try:
		videos = paginator1.page(page)
	except PageNotAnInteger:
		videos = paginator1.page(1)
	except EmptyPage:
		videos = paginator1.page(paginator.num_pages)

	return render(request,'detalheCurso.html',{'cursos':cursos,'curso':curso,'imagem':imagem,'noticias':noticias,'videos':videos,'page':page})

def DetalhesNoticias(request,id):
	cursos = Curso.objects.all()
	noticia = Noticia.objects.get(id=id)
	#filra a id certa e traz anoticia desta id
	noticias = Noticia.objects.all().filter(id = id )
	imagens = Imagen.objects.all().filter(idnoticia=id).order_by("-id")
	paginator = Paginator(imagens,4)
	page = request.GET.get('page')
	try:
		imagens = paginator.page(page)
	except PageNotAnInteger:
		imagens = paginator.page(1)
	except EmptyPage:
		imagens = paginator.page(paginator.num_pages)
	return render(request,'detalhenoticias.html',{'noticia':noticia,'noticias':noticias,'cursos':cursos,'imagens':imagens,'page':page})


def agronomia(request):
	cursos = Curso.objects.all()
	imagem= Imagen.objects.all()
	noticias = Noticia.objects.all()
	return render(request,'agronomia.html',{'cursos':cursos,'imagem':imagem,'noticias':noticias})

def engenharia_ambiental(request):
	cursos = Curso.objects.all()
	return render(request,'engenharia_ambiental.html',{'cursos':cursos})


def jornalismo(request):
	cursos = Curso.objects.all()
	return render(request,'jornalismo.html',{'cursos':cursos})

def engenharia_florestal(request):
	cursos = Curso.objects.all()
	return render(request,'engenharia_florestal.html',{'cursos':cursos})


def relacoes_publicas(request):
	cursos = Curso.objects.all()
	return render(request,'relacoes_publicas.html',{'cursos':cursos})

def sistemas_informacao(request):
	cursos = Curso.objects.all()
	return render(request,'sistemas_informacao.html',{'cursos':cursos})

def alimentacao(request):
	cursos = Curso.objects.all()
	alimentacao = Alimentacao.objects.all()
	return render(request,'alimentacao.html',{'alimentacao':alimentacao,'cursos':cursos})

def hospedagem (request):
	cursos = Curso.objects.all()
	hospedagem = Hotei.objects.all()
	return render(request,'hospedagem.html',{'hospedagem':hospedagem,'cursos':cursos})

def moradia (request):
	cursos = Curso.objects.all()
	moradia = Imobiliaria.objects.all()
	return render(request,'moradia.html',{'moradia':moradia,'cursos':cursos})


def contatos (request):
	cursos = Curso.objects.all()
	contatos = Contato.objects.all()
	return render(request,'contatos.html',{'contatos':contatos,'cursos':cursos})

def assistencia(request):
	cursos = Curso.objects.all()
	return render(request,'assistencia.html',{'cursos':cursos})

def horario(request):
	cursos = Curso.objects.all()
	return render(request,'horario.html',{'cursos':cursos})


def galeria(request):
	cursos = Curso.objects.all()
	imagem= Imagen.objects.all().order_by("-id")
	videos = Video.objects.all().order_by("-id")
	paginator = Paginator(imagem,8)
	paginator_ = Paginator(videos,3)

	page = request.GET.get('page')
	try:
		imagem = paginator.page(page)
	except PageNotAnInteger:
		imagem = paginator.page(1)
	except EmptyPage:
		imagem = paginator.page(paginator.num_pages)

	try: 
		videos = paginator_.page(page)
	except PageNotAnInteger:
		videos = paginator_.page(1)
	except EmptyPage:
		videos = pagi.page(paginator_.num_pages)

	return render(request,'galeria.html',{'imagem':imagem,'videos':videos,'cursos':cursos,'page':page,})


def edital(request):
	cursos = Curso.objects.all()
	arquivos = Edital.objects.all().order_by("-id")
	paginator = Paginator(arquivos,10)
	page = request.GET.get('page')
	try:
		arquivos = paginator.page(page)
	except PageNotAnInteger:
		arquivos = paginator.page(1)
	except EmptyPage:
		arquivos = paginator.page(paginator.num_pages)



	return render (request,'arquivos.html',{'arquivos':arquivos,'page':page,'cursos':cursos})

def contatos_oficiais(request):
	cursos = Curso.objects.all()
	contatos_oficiais = Contato_Administrativo.objects.all()

	return render (request,'contatos_oficiais.html',{'contatos_oficiais':contatos_oficiais,'cursos':cursos})

