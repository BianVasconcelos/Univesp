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
    
class Pedido(models.Model):
    TIPOS_PAGAMENTO = (
        ('Dinheiro', 'Dinheiro'),
        ('Debito', 'Debito'),
        ('Credito', 'Credito'),        
    )
    data_hora = models.DateTimeField()
    valor_total = models.DecimalField(max_digits=5, decimal_places=2)
    tipo_pagamento = models.CharField(max_length=15, choices=TIPOS_PAGAMENTO)
    pedido = models.ForeignKey("Pessoa", on_delete=models.CASCADE, related_name='pedidos')
    login = models.ForeignKey("Login", on_delete=models.CASCADE, related_name='pedidos')
    
    def __str__(self):
        return f"{self.pedido} - {self.valor_total}"
    
class Login(models.Model):
    TIPOS_USUARIO = (
        ('Adm', 'Administrador'),
        ('Com', 'Comum'),
    )
    usuario = models.CharField(max_length=45)
    senha = models.CharField(max_length=45)
    tipo_user = models.CharField(max_length=20, choices=TIPOS_USUARIO)
    
    def __str__(self):
        return f"{self.usuario}"

class ItensPedido(models.Model):
    item_id = models.IntegerField()
    tipo_item = models.CharField(max_length=10)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=5, decimal_places=2)
    
    pizza = models.ForeignKey("Pizza", on_delete=models.CASCADE, related_name='ItensPedido')
    pedido = models.ForeignKey("Pedido", on_delete=models.CASCADE, related_name='ItensPedido')
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE, related_name='ItensPedido')
    
    def __str__(self):
        return f"{self.item_id} {self.tipo_item} - {self.quantidade} {self.preco_unitario}, ({self.pedido}, {self.produto}) "    