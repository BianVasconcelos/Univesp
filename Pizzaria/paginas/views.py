from django.views.generic import TemplateView

# Create your views here.
#class PaginaInicial(TemplateView):
#    template_name = "paginas/index.html"
    
class PaginaInicial(TemplateView):
    template_name = "paginas/pizzalist.html"
    
class SobreView(TemplateView):
    template_name = "paginas/sobre.html"