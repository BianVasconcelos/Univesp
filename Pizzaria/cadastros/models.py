from django.db import models

# Create your models here.

class Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    endereco = models.CharField(max_length=100, verbose_name='Endereço', blank=False, null=False)
    numero = models.CharField(max_length=10, blank=False, null=False)
    cep = models.CharField(max_length=10, blank=False, null=False)
    bairro = models.CharField(max_length=50, blank=False, null=False)
    cidade = models.CharField(max_length=100, blank=False, null=False)
    estado = models.CharField(max_length=4, blank=False, null=False)
    
    def __str__(self):
        return f"{self.endereco}, {self.numero} - ({self.cep}), {self.bairro}, {self.cidade} - {self.estado}"
    
class Clientes(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(null=False, blank=False)
    
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.nome}"
    
class Fornecedores(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(null=False, blank=False)
    
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.nome}"

    
