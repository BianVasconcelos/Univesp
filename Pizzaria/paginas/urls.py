from django.urls import path

#Importa view que foi criada 
from .views import PaginaInicial, SobreView

urlpatterns = [
   path('', PaginaInicial.as_view(), name='home'),
   path('sobre/', SobreView.as_view(), name='sobre'), 
]
