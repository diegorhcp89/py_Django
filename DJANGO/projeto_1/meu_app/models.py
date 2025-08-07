from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome
