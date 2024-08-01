from typing import Counter
from django.shortcuts import render, redirect
from .models import Genero,Pelicula,Director,Pais,Cine
from django.contrib import messages 
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')
# Renderizando el template de listadoDirectores
def listadoDirectores(request):
    directoresBdd=Director.objects.all()
    return render(request,'listadoDirectores.html', {'directores':directoresBdd})
def eliminarDirector(request,id):
    directorEliminar=Director.objects.get(id=id)
    directorEliminar.delete()
    messages.success(request,'director eliminado con exito')
    return redirect('listadoDirectores')
def nuevoDirector(request):
    return render(request,'nuevoDirector.html')
def guardarDirector(request):
    dni=request.POST['dni']
    apellido=request.POST['apellido']
    nombre=request.POST['nombre']
    estado=request.POST['estado']
    foto=request.FILES.get("foto")
    nuevoDirector=Director.objects.create(dni=dni,apellido=apellido,nombre=nombre,estado=estado,foto=foto)
    messages.success(request,'Director guardado con éxito')
    return redirect('listadoDirectores')
def editarDirector(request,id):
    directorEditar=Director.objects.get(id=id)
    return render(request,'editarDirector.html',{'director':directorEditar})

def procesarActualizacionesDirector(request):
    id=request.POST['id']
    dni=request.POST['dni']
    apellido=request.POST['apellido']
    nombre=request.POST['nombre']
    estado=request.POST['estado']
    directorConsultado=Director.objects.get(id=id)
    directorConsultado.dni=dni
    directorConsultado.apellido=apellido
    directorConsultado.nombre=nombre
    directorConsultado.estado=estado
    directorConsultado.save()
    messages.success(request,'Director actualizado con éxito')
    return redirect('listadoDirectores')
# Renderizando el template de ListadoGenero
def listadoGeneros(request):
    generosBdd = Genero.objects.all()
    # Contar descripciones por cada género
    genero_counts = Counter([genero.nombre for genero in generosBdd])
    context = {
        'generos': generosBdd,
        'nombres': list(genero_counts.keys()), # Nombres de los géneros
        'descripciones_count': list(genero_counts.values()) # Conteo de descripciones por género
    }
    return render(request, 'listadoGeneros.html', context)
#Se recibe el id para eliminar un genero
def eliminarGenero(request,id):
    generoEliminar = Genero.objects.get(id=id)
    generoEliminar.delete()
    messages.success(request, 'Genero eliminado con éxito')
    return redirect('listadoGeneros')
#Redenrizando formulario del nuevoGenero
def nuevoGenero(request):
    return render(request,'nuevoGenero.html')

def guardarGenero(request):
    nom=request.POST['nombre']
    desc=request.POST['descripcion']
    foto=request.FILES.get("foto")
    nuevoGenero=Genero.objects.create(nombre=nom,descripcion=desc,foto=foto)
    messages.success(request, 'Genero guardado con éxito')
    return redirect('listadoGeneros')

#renderizar formulario de actualizacion
def editarGenero(request,id):
    generoEditar = Genero.objects.get(id=id)
    return render(request, 'editarGenero.html', {'generoEditar':generoEditar})
#actualizancdo los nuevos datos de la BDD
def procesarActualizacionesGenero(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    descripcion=request.POST['descripcion']
    generoConsultado = Genero.objects.get(id=id)
    generoConsultado.nombre=nombre #cambiamos datos en la BDD
    generoConsultado.descripcion=descripcion
    generoConsultado.save() #confirma datos en la BDD
    messages.success(request, 'Genero actualizado con éxito')
    return redirect('listadoGeneros')

def listadoPais(request):
    paisesBdd=Pais.objects.all()
    return render(request, 'listadoPais.html', {'paises': paisesBdd})

#Se recibe el id para eliminar un pais
def eliminarPais(request,id):
    paisEliminar = Pais.objects.get(id=id)
    paisEliminar.delete()
    messages.success(request, 'pais eliminado con éxito')
    return redirect('listadoPais')

def nuevoPais(request):
    return render(request, 'nuevoPais.html')

def guardarPais(request):
    nom=request.POST['nombre']
    capit=request.POST['capital']
    foto=request.FILES.get("foto")
    nuevoPais=Pais.objects.create(nombre=nom,capital=capit)
    messages.success(request, 'Pais guardado con éxito')
    return redirect('listadoPais')

#renderizar formulario de actualacion pais
def editarPais(request,id):
    paisEditar = Pais.objects.get(id=id)
    return render(request, 'editarPais.html', {'paisEditar':paisEditar})

#actualizancdo los nuevos datos de la BDD
def procesarActualizacionesPais(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    continente=request.POST['continente']
    capital=request.POST['capital']
    paisConsultado= Pais.objects.get(id=id)
    paisConsultado.nombre=nombre
    paisConsultado.continente=continente
    paisConsultado.capital=capital
    paisConsultado.save()
    messages.success(request, 'Pais actualizado con éxito')
    return redirect('listadoPais')

    
# Renderizando el template de ListadoPeliculas
def listadoPeliculas(request):
    peliculasBdd=Pelicula.objects.all()
    return render(request,'listadoPeliculas.html', {'peliculas':peliculasBdd})


def gestionCines(request):
    return render(request,'gestionCines.html')

def guardarCine(request):
    nom=request.POST['nombre']
    dir=request.POST['direccion']
    tel=request.POST['telefono']
    nuevoCine=Cine.objects.create(nombre=nom,direccion=dir,telefono=tel)
    return JsonResponse({
        'estado':True,
        'mensaje':'Cine registrado exitosamente',
    })
#renderizar el listado de cines
def listadoCines(request):
    cines=Cine.objects.all()
    return render(request,'listadoCines.html',{'cines':cines})

# director fetch

def director(request):
    return render(request,'director.html')

def listaDirector(request):
    directores=Director.objects.all()
    return render(request,'listaDirector.html',{'directores':directores})

#Guardar Director
def guardarDirector(request):
    dni=request.POST['dni']
    nom=request.POST['nombre']
    ape=request.POST['apellido']
    fot=request.FILES.get("foto")
    nuevoDirector=Director.objects.create(dni=dni,nombre=nom,apellido=ape,foto=fot)
    return JsonResponse({'estado': True, 'mensaje': 'Director guardado correctamente'})


# Pelicula fetch
def pelicula(request):
    return render(request,'pelicula.html')

def listaPelicula(request):
    peliculas=Pelicula.objects.all()
    return render(request,'listaPelicula.html',{'peliculas':peliculas})

#Guardar Pelicula
def guardarPelicula(request):
    tit=request.POST['titulo']
    dura=request.POST['duracion']
    sin=request.POST['sinopsis']
    nuevoPelicula=Pelicula.objects.create(titulo=tit,duracion=dura,sinopsis=sin)
    return JsonResponse({'estado': True, 'mensaje': 'Pelicula guardado correctamente'})