from django.db import models
from django.utils import timezone

# Create your models here.

class ArtigoPrincipal(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='media/', blank=True, null=True)
    def __str__(self):
        return self.titulo

class ArtigoSecundario(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='media/', blank=True, null=True)
    def __str__(self):
        return self.titulo

class ArtigoTerceiro(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='media/', blank=True, null=True)
    def __str__(self):
        return self.titulo


class ArtigosGenericos(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='media/', blank=True, null=True)
    def __str__(self):
        return self.titulo

class ArtigosRecommends(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='media/', blank=True, null=True)
    def __str__(self):
        return self.titulo



