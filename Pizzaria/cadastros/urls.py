from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

#Importa as view que foi criada
from .views import PessoaCreate, PessoaUpdate, PessoaDelete
from .views import PizzaCreate, PizzaUpdate, PizzaDelete
from .views import ProdutoCreate, ProdutoUpdate, ProdutoDelete
from .views import PedidoCreate, PedidoUpdate, PedidoDelete
from .views import LoginCreate, LoginUpdate, LoginDelete
from .views import ItensPedidoCreate, ItensPedidoUpdate, ItensPedidoDelete
from .views import PessoaList, PizzaList, ProdutoList, PedidoList, ItensPedidoList, LoginList, HomePageList


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
    
    path('cadastrar/pedido', PedidoCreate.as_view(), name='cadastrar-pedido'),        
    path('editar/pedido/<int:pk>/', PedidoUpdate.as_view(), name='editar-pedido'),   
    path('excluir/pedido/<int:pk>', PedidoDelete.as_view(), name='excluir-pedido'), 
    
    path('cadastrar/login', LoginCreate.as_view(), name='cadastrar-login'),        
    path('editar/login/<int:pk>/', LoginUpdate.as_view(), name='editar-login'),   
    path('excluir/login/<int:pk>', LoginDelete.as_view(), name='excluir-login'),
    
    path('cadastrar/itenspedido', ItensPedidoCreate.as_view(), name='cadastrar-itenspedido'),        
    path('editar/itenspedido/<int:pk>/', ItensPedidoUpdate.as_view(), name='editar-itenspedido'),   
    path('excluir/itenspedido/<int:pk>', ItensPedidoDelete.as_view(), name='excluir-itenspedido'),
    
    path('listar/pessoas/', PessoaList.as_view(), name='listar-pessoas'),
    path('listar/pedidos/', PedidoList.as_view(), name='listar-pedidos'),
    path('listar/produtos/', ProdutoList.as_view(), name='listar-produtos'),
    path('listar/pizzas/', PizzaList.as_view(), name='listar-pizzas'),
    path('listar/itenspedidos/', ItensPedidoList.as_view(), name='listar-itenspedidos'),
    path('listar/logins/', LoginList.as_view(), name='listar-logins'),
    path('listar/listpizza/', HomePageList.as_view(), name='listpizza'),
    path('home', HomePageList.as_view(), name='home'),            
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)