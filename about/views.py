from django.shortcuts import render

# Create your views here.
def about(request):
    """
    Render al HTML de about
    """
    imagen_de_fondo_ccs = 'about'
    active_nav = 'about'
    contexto = {
        'imagen_ccs': imagen_de_fondo_ccs,
        'active_nav': active_nav
    }
    return render(request, 'core/about.html', contexto)