from django.contrib import admin

#Importar as classes
from .models import Pessoa, Pizza, Produto

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Pizza)
admin.site.register(Produto)
