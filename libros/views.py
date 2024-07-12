from django.shortcuts import render
from .models import Navbar
from .models import Libro
from .models import Autor
from .models import Categoria

def index(request):
    navbar_items = Navbar.objects.all()
    libros = Libro.objects.all()
    context = {
        "navbar_items": navbar_items,
        "libros": libros,
    }
    return render(request, 'libros/index.html', context)
	
def lista_libros(request):
    libros = Libro.objects.all()
    context = {
        "libros": libros
    }
    return render(request, 'libros/libros.html', context)
	
def autor(request):
    autores = Autor.objects.all()
    context = {
        "autores": autores
    }
    return render(request, 'libros/autor.html', context)
	
def categoria(request):
    categorias = Categoria.objects.all()
    context = {
        "categorias": categorias
    }
    return render(request, 'libros/categoria.html', context)
