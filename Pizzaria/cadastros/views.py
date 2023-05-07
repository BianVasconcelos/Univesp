from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Clientes, Fornecedores, Endereco

from django.urls import reverse_lazy

# Create your views here.
class ClientesCreate(CreateView):
    model = Clientes
    fields = [
        'nome',
        'endereco',
        'telefone',
        'email'
    ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
class FornecedoresCreate(CreateView):
    model = Fornecedores
    fields = [
        'nome',
        'endereco',
        'telefone',
        'email'
    ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
class EnderecoCreate(CreateView):
    model = Endereco
    fields = [
        'endereco',
        'numero',
        'cep',
        'bairro',
        'cidade',
        'estado'
    ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
####################### UPDATE ####################### 
class ClientesUpdate(UpdateView):
   model = Clientes
   fields = [
        'nome',
        'endereco',
        'telefone',
        'email'
   ]
   template_name = 'cadastros/form.html'
   success_url = reverse_lazy('index')
    
class FornecedoresUpdate(UpdateView):
    model = Fornecedores
    fields = [
        'nome',
        'endereco',
        'telefone',
        'email'
    ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
class EnderecoUpdate(UpdateView):
    model = Endereco
    fields = [
        'endereco',
        'numero',
        'cep',
        'bairro',
        'cidade',
        'estado'
    ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')    
    
####################### DELETE ####################### 
class ClientesDelete(DeleteView):
   model = Clientes
   template_name = 'cadastros/form-excluir.html'
   success_url = reverse_lazy('index')
    
class FornecedoresDelete(DeleteView):
    model = Fornecedores
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
    
class EnderecoDelete(DeleteView):
    model = Endereco
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')