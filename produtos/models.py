from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    marca = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    imagem = models.ImageField(upload_to='imagem')
    descricao = models.TextField()
    def __str__(self):
        return self.nome
    



# Create your models here.
