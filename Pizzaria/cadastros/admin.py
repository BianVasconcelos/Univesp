from django.contrib import admin

#Importar as classes
from .models import Pessoa, Pizza, Produto, Login, Pedido, ItensPedido, Fornecimento

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Pizza)
admin.site.register(Produto)
admin.site.register(Login)
admin.site.register(Pedido)
admin.site.register(ItensPedido)
admin.site.register(Fornecimento)
