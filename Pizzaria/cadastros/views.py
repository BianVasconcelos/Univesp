from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Pessoa, Pizza, Produto, Pedido, Login, ItensPedido

from django.urls import reverse_lazy

# Create your views here.
class PessoaCreate(CreateView):
    model = Pessoa
    fields = [
        'tipo',
        'nome',
        'telefone',
        'email',
        'endereco',
        'numero',
        'complemento',
        'bairro',
        'cidade',
        'estado',
        'cep'
    ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
class PizzaCreate(CreateView):
    model = Pizza
    fields = [
       'nome',
       'valor_p',
       'valor_m',
       'valor_g',
       'descricao'
    ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
class ProdutoCreate(CreateView):
    model = Produto
    fields = [
        'nome',
        'preco',
        'descricao',
        'fornecedores'
    ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class PedidoCreate(CreateView):
    model = Pedido
    fields = [
        'data_hora',
        'valor_total',
        'pessoa',
        'login'        
    ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class LoginCreate(CreateView):
    model = Login
    fields = [
        'usuario',
        'senha'
    ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')           

class ItensPedidoCreate(CreateView):
    model = ItensPedido
    fields = [
        'item_id',
        'tipo_item',
        'quantidade',
        'preco_unitario',
        'pedido',
        'pizza'
    ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')  
####################### UPDATE ####################### 
class PessoaUpdate(UpdateView):
   model = Pessoa
   fields = [
        'tipo',
        'nome',
        'telefone',
        'email',
        'endereco',
        'numero',
        'complemento',
        'bairro',
        'cidade',
        'estado',
        'cep'
    ]
   template_name = 'cadastros/form.html'
   success_url = reverse_lazy('index')
   
class PizzaUpdate(UpdateView):
    model = Pizza
    fields = [
       'nome',
       'valor_p',
       'valor_m',
       'valor_g',
       'descricao',
       'imagem'
    ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
class ProdutoUpdate(UpdateView):
    model = Produto
    fields = [
        'nome',
        'preco',
        'descricao',
        'fornecedores'
    ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class PedidoUpdate(UpdateView):
    model = Pedido
    fields = [
        'data_hora',
        'valor_total',
        'pessoa',
        'login'        
    ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
class LoginUpdate(UpdateView):
    model = Login
    fields = [
        'usuario',
        'senha'
    ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
class ItensPedidoUpdate(UpdateView):
    model = ItensPedido
    fields = [
        'item_id',
        'tipo_item',
        'quantidade',
        'preco_unitario',
        'pedido',
        'pizza'
    ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
####################### DELETE ####################### 
class PessoaDelete(DeleteView):
   model = Pessoa
   template_name = 'cadastros/form-excluir.html'
   success_url = reverse_lazy('index')
   
class PizzaDelete(DeleteView):
   model = Pizza
   template_name = 'cadastros/form-excluir.html'
   success_url = reverse_lazy('index')
   
class ProdutoDelete(DeleteView):
   model = Produto
   template_name = 'cadastros/form-excluir.html'
   success_url = reverse_lazy('index')
   
class PedidoDelete(DeleteView):
   model = Pedido
   template_name = 'cadastros/form-excluir.html'
   success_url = reverse_lazy('index')
      
class LoginDelete(DeleteView):
   model = Login
   template_name = 'cadastros/form-excluir.html'
   success_url = reverse_lazy('index')
    
class ItensPedidoDelete(DeleteView):
    model = ItensPedido
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')