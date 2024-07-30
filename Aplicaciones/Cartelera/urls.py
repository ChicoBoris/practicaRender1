from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    # géneros
    path('listadoGeneros/', views.listadoGeneros, name='listadoGeneros'),
    path('eliminarGenero/<id>', views.eliminarGenero, name='eliminarGenero'),
    path('nuevoGenero/', views.nuevoGenero, name='nuevoGenero'),
    path('guardarGenero/', views.guardarGenero, name='guardarGenero'),
    path('editarGenero/<id>', views.editarGenero, name='editarGenero'),
    path('procesarActualizacionesGenero/', views.procesarActualizacionesGenero, name='procesarActualizacionesGenero'),  # <- Coma añadida aquí
    # películas
    path('listadoPeliculas/', views.listadoPeliculas),
    # directores
    path('listadoDirectores/', views.listadoDirectores, name='listadoDirectores'),
    path('eliminarDirector/<id>', views.eliminarDirector, name='eliminarDirector'),
    path('nuevoDirector/', views.nuevoDirector, name='nuevoDirector'),
    path('guardarDirector/', views.guardarDirector, name='guardarDirector'),
    path('editarDirector/<id>', views.editarDirector, name='editarDirector'),
    path('procesarActualizacionesDirector/', views.procesarActualizacionesDirector, name='procesarActualizacionesDirector'),  # <- Coma añadida aquí
    # país
    path('listadoPais/', views.listadoPais, name='listadoPais'),
    path('eliminarPais/<id>', views.eliminarPais, name='eliminarPais'),
    path('nuevoPais/', views.nuevoPais, name='nuevoPais'),
    path('guardarPais/', views.guardarPais, name='guardarPais'),
    path('editarPais/<id>', views.editarPais, name='editarPais'),
    path('procesarActualizacionesPais/', views.procesarActualizacionesPais, name='procesarActualizacionesPais'),  # <- Coma añadida aquí
    
    path('gestionCines/',views.gestionCines, name='gestionCines'),
    path('guardarCine/', views.guardarCine, name='guardarCine'),
    
    path('listadoCines/', views.listadoCines, name='listadoCines'),
    
    #Director fetch
    path('director/',views.director, name="director"),
    path('listaDirector/',views.listaDirector, name="listaDirector"),
    
    #Pelicula Fetch
    path('pelicula/',views.pelicula, name="pelicula"),
    path('listaPelicula/',views.listaPelicula, name="listaPelicula"),
    path('guardarPelicula/',views.guardarPelicula, name="guardarPelicula"),
    
    
    path('generos/', views.listadoGeneros, name='listadoGeneros'),
    path('generos/nuevo/', views.nuevoGenero, name='nuevoGenero'),
]
