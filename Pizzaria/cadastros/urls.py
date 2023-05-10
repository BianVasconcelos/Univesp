from django.urls import path

#Importa as view que foi criada
from .views import PessoaCreate, PessoaUpdate, PessoaDelete
from .views import PizzaCreate, PizzaUpdate, PizzaDelete
from .views import ProdutoCreate, ProdutoUpdate, ProdutoDelete


urlpatterns = [
    #path('', PaginaIncial.as_view(), name='index'),
    path('cadastrar/pessoa', PessoaCreate.as_view(), name='cadastrar-pessoa'),        
    path('editar/pessoa/<int:pk>/', PessoaUpdate.as_view(), name='editar-pessoa'),   
    path('excluir/pessoa/<int:pk>', PessoaDelete.as_view(), name='excluir-pessoa'),
    
    path('cadastrar/pizza', PizzaCreate.as_view(), name='cadastrar-pizza'),        
    path('editar/pizza/<int:pk>/', PizzaUpdate.as_view(), name='editar-pizza'),   
    path('excluir/pizza/<int:pk>', PizzaDelete.as_view(), name='excluir-pizza'),
    
    path('cadastrar/produto', ProdutoCreate.as_view(), name='cadastrar-produto'),        
    path('editar/produto/<int:pk>/', ProdutoUpdate.as_view(), name='editar-produto'),   
    path('excluir/produto/<int:pk>', ProdutoDelete.as_view(), name='excluir-produto'),           
]