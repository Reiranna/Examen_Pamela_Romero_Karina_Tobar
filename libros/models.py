from django.db import models

# Create your models here.

class Navbar(models.Model):
    titulo = models.CharField(primary_key=True, max_length=200)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.titulo

class Libro(models.Model):
    codigo = models.CharField(primary_key=True, max_length=20, unique=True)
    titulo_libro = models.CharField(max_length=60)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE, db_column='nom_autor')
    anio_publicacion = models.DateField()
    descripcion = models.CharField(max_length=200)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, db_column='nom_categoria')

    def __str__(self):
        return self.titulo_libro

class Autor(models.Model):
    nombre = models.CharField(db_column='nom_autor', primary_key=True, max_length=60)
    nacionalidad = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre_cat = models.CharField(primary_key=True, db_column='nom_categoria', max_length=60)
    descripcion_cat = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_cat
