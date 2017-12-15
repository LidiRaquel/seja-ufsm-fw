
from django.db import models
import datetime

class Curso (models.Model):
	Logo = models.ImageField(upload_to='logos', blank=True,null=True)
	Nome = models.CharField(max_length =100, blank=True)
	Vagas = models.CharField(max_length =100, blank=True)
	Duracao = models.CharField(max_length =100, blank=True,verbose_name='Duração')
	Turno = models.CharField(max_length =100, blank=True)
	Objetivo = models.TextField(blank=True)
	Perfil = models.TextField(blank=True)
	Atuacao = models.TextField(blank=True,verbose_name='Atuação')
	Coordenador = models.CharField(max_length =100, blank=True)
	Telefone = models.CharField(max_length =100, blank=True)
	Email = models.EmailField(max_length =100, blank=True)
	Grade =  models.URLField(max_length=300,blank=True)

	def __str__(self):
		return self.Nome

class Alimentacao (models.Model):
	Nome = models.CharField(max_length =100,blank=True)
	Endereco = models.CharField(max_length =100,blank=True,verbose_name='Endereço')
	Telefone = models.CharField(max_length =100,blank=True)

	def __str__(self):
		return self.Nome

class Hotei (models.Model):
	"""docstring for Hospedagem """
	Nome = models.CharField(max_length =100,blank=True)
	Endereco = models.CharField(max_length =100,blank=True,verbose_name='Endereço')
	Telefone = models.CharField(max_length =100,blank=True)
	Site =  models.URLField(max_length=300,blank=True)
	def __str__(self):
		return self.Nome

class Imobiliaria (models.Model):
	Nome = models.CharField(max_length =100,blank=True)
	Endereco = models.CharField(max_length =100,blank=True,verbose_name='Endereço')
	Telefone = models.CharField(max_length =100,blank=True)
	Site =  models.URLField(max_length=300,blank=True)
	def __str__(self):
		return self.Nome

class Contato(models.Model):
	Nome = models.CharField(max_length = 100,blank=True)
	Telefone = models.CharField(max_length = 100,blank=True)
	Email = models.CharField(max_length = 100,blank=True)
	def __str__(self):
		return self.Nome



class Noticia(models.Model):
	idcurso = models.ForeignKey('Curso',on_delete=models.CASCADE,blank=True,null=True,verbose_name='Curso' )
	Titulo = models.CharField(max_length= 100, blank=True,)
	Data = models.DateField(blank=True)
	Descricao = models.CharField(max_length =150, blank=True,verbose_name='Descrição')
	Texto = models.TextField( blank=True)
	def __str__(self):
		return self.Titulo

class Imagen (models.Model):
	idcurso = models.ForeignKey('Curso',on_delete=models.CASCADE,blank=True,null=True,verbose_name='Curso')
	idnoticia = models.ForeignKey('Noticia',on_delete=models.CASCADE,blank=True,null=True,verbose_name='Notícia')
	Titulo = models.CharField(max_length=100,blank=True)
	Imagem = models.ImageField(null=True,blank=True,upload_to='galeria')
	def __str__(self):
		return self.Titulo


class Edital(models.Model):
	Data = models.DateField(blank=True)
	Nome = models.CharField(max_length=100, blank=True)
	Arquivo = models.FileField(upload_to='media/arquivos', blank=True)
	def __str__(self):
		return self.Nome

class Contato_Administrativo(models.Model):
	Nome=models.CharField(max_length=100,blank=True)
	Setor = models.CharField(max_length = 100, blank=True)
	Telefone = models.CharField(max_length = 100,blank=True)
	Email = models.CharField(max_length = 100,blank=True)
	Site =  models.URLField(max_length=300,blank=True)
	def __str__(self):
		return self.Nome

class Video(models.Model):
	Nome: models.CharField(max_length=100,blank=True)
	URL = models.URLField(max_length=300, blank=True)
	def __str__(self):
		return self.Nome