from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('libros/', views.lista_libros, name='lista_libros'),
    path('autores/', views.autor, name='autor'),
    path('categorias/', views.categoria, name='categoria'),
]
