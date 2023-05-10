from django.db import models

# Create your models here.

class Pessoa(models.Model):
    TIPOS_PESSOA = (
        ('Cliente', 'Cliente'),
        ('Fornecedor', 'Fornecedor'),
    )
    tipo = models.CharField(max_length=10, choices=TIPOS_PESSOA)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    endereco = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nome
    
class Pizza(models.Model):
    nome = models.CharField(max_length=100)
    valor_p = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Valor P')
    valor_m = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Valor M')
    valor_g = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Valor G')
    descricao = models.CharField(max_length=255, verbose_name='Descrição')
    imagem = models.ImageField(upload_to='static/img', null=True, blank=True)
    
    def __str__(self):
        return f"{self.nome}"
    
class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Preço')
    descricao = models.CharField(max_length=255, verbose_name='Descrição')
    fornecedores = models.ManyToManyField(Pessoa, through='Fornecimento', related_name='produtos', blank=True)
    
    def __str__(self):
        return f"{self.nome}"
    
class Fornecimento(models.Model):
    fornecedor = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
