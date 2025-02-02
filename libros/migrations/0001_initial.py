# Generated by Django 5.0.7 on 2024-07-12 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('nombre', models.CharField(db_column='nom_autor', max_length=60, primary_key=True, serialize=False)),
                ('nacionalidad', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('nombre_cat', models.CharField(db_column='nom_categoria', max_length=60, primary_key=True, serialize=False)),
                ('descripcion_cat', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('codigo', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('titulo_libro', models.CharField(max_length=60)),
                ('anio_publicacion', models.DateField()),
                ('descripcion', models.CharField(max_length=200)),
                ('autor', models.ForeignKey(db_column='nom_autor', on_delete=django.db.models.deletion.CASCADE, to='libros.autor')),
                ('categoria', models.ForeignKey(db_column='nom_categoria', on_delete=django.db.models.deletion.CASCADE, to='libros.categoria')),
            ],
        ),
    ]
