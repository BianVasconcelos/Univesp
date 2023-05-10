from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Pessoa, Pizza, Produto

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
    
    def form_valid(self, form):
        fornecedor_id = self.request.POST.get('fornecedor')
        fornecedor = Pessoa.objects.get(id=fornecedor_id)
        produto = form.save(commit=False)
        produto.save()
        produto.fornecedores.add(fornecedor)
        return super().form_valid(form)
           
  
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
    
    def form_valid(self, form):
        fornecedor_id = self.request.POST.get('fornecedor')
        fornecedor = Pessoa.objects.get(id=fornecedor_id)
        produto = form.save(commit=False)
        produto.save()
        produto.fornecedores.add(fornecedor)
        return super().form_valid(form)   
    
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
