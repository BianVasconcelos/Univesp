from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Pessoa, Pizza, Produto, Pedido, Login, ItensPedido

from .forms import PizzaForm

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
    template_name = 'cadastros/formpessoa.html'
    success_url = reverse_lazy('listar-pessoas')
    
class PizzaCreate(CreateView):
    model = Pizza
    form_class = PizzaForm    
    template_name = 'cadastros/formpizza.html'
    success_url = reverse_lazy('listar-pizzas')
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
class ProdutoCreate(CreateView):
    model = Produto
    fields = [
        'nome',
        'preco',
        'descricao',
        'fornecedores'
    ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtos')

class PedidoCreate(CreateView):
    model = Pedido
    fields = [
        'data_hora',
        'valor_total',
        'pessoa',
        'login'        
    ]
    template_name = 'cadastros/formpedido.html'
    success_url = reverse_lazy('listar-pedidos')

class LoginCreate(CreateView):
    model = Login
    fields = [
        'usuario',
        'senha'
    ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-logins')           

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
    success_url = reverse_lazy('listar-itenspedidos')  
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
    template_name = 'cadastros/formpizza.html'
    form_class = PizzaForm
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
    success_url = reverse_lazy('listar-produtos')

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
    
####################### LISTAR #######################

class PessoaList(ListView):
    model = Pessoa
    template_name = 'cadastros/listas/pessoa.html'
    
class PizzaList(ListView):
    model = Pizza
    template_name = 'cadastros/listas/pizza.html'
    
class ProdutoList(ListView):
    model = Produto
    template_name = 'cadastros/listas/produto.html'    

class PedidoList(ListView):
    model = Pedido
    template_name = 'cadastros/listas/pedido.html'
    
class ItensPedidoList(ListView):
    model = ItensPedido
    template_name = 'cadastros/listas/itenspedido.html'
    
class LoginList(ListView):
    model = Login
    template_name = 'cadastros/listas/login.html'
    
class HomePageList(ListView):
    model = Pizza
    template_name = 'paginas/pizzalist.html'
    context_object_name = 'pizza'  
