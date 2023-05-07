from django.contrib import admin

#Importar as classes
from .models import Endereco, Clientes, Fornecedores

# Register your models here.
admin.site.register(Endereco)
admin.site.register(Clientes)
admin.site.register(Fornecedores)
