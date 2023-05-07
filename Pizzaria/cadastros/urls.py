from django.urls import path

#Importa as view que foi criada
from .views import ClientesCreate, FornecedoresCreate, EnderecoCreate
from .views import ClientesUpdate, FornecedoresUpdate, EnderecoUpdate
from .views import ClientesDelete, FornecedoresDelete, EnderecoDelete

urlpatterns = [
    #path('', PaginaIncial.as_view(), name='index'),
    path('cadastrar/clientes', ClientesCreate.as_view(), name='cadastrar-clientes'),
    path('cadastrar/fornecedores', FornecedoresCreate.as_view(), name='cadastrar-fornecedores'),
    path('cadastrar/enderecos', EnderecoCreate.as_view(), name='cadastrar-enderecos'),
    
    path('editar/clientes/<int:pk>/', ClientesUpdate.as_view(), name='editar-clientes'),
    path('editar/fornecedores/<int:pk>', FornecedoresUpdate.as_view(), name='editar-fornecedores'),
    path('editar/enderecos/<int:pk>', EnderecoUpdate.as_view(), name='editar-enderecos'),
    
    path('excluir/clientes/<int:pk>', ClientesDelete.as_view(), name='excluir-clientes'),
    path('excluir/Fornecedores/<int:pk>', FornecedoresDelete.as_view(), name='excluir-fornecedores'), 
    path('excluir/enderecos/<int:pk>', EnderecoDelete.as_view(), name='excluir-enderecos'),        
]