from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .forms import AlbumForm, GrupoForm, MusicoForm
from .models import Album, Grupo, Musico
import requests
import json
import gc

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def test(request):
    return HttpResponse('¡Segunda vista!')

def profile(request):

    return render(request, 'practica_08/estadisticas.html')

def music(request):        
    return render(request, 'practica_08/estadisticas.html')

#-------Añadir nuevos objetos a la BD------------------------------------------------
def nuevoAlbum(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)

        if form.is_valid():
            post = form.save()
            post.save()

            return redirect('datosAlbum', pk=post.pk)
            # return HttpResponse("Vale, tá bien.")
    else:
        form = AlbumForm()

    return render(request, 'practica_08/album_add.html', {'form': form})

def nuevoGrupo(request):
    if request.method == "POST":
        form = GrupoForm(request.POST)
        
        if form.is_valid():
            post = form.save()
            post.save()
            
            return redirect('datosGrupo', pk=post.pk)
            #return render(request, "practica_08/datos.html", {'post': post, 'pk': post.pk})
    else:
        form = GrupoForm()
    
    return render(request, "practica_08/grupo_add.html", {'form': form})

def nuevoMusico(request):
    if request.method == "POST":
        form = MusicoForm(request.POST)

        if form.is_valid():
            post = form.save()
            post.save()

            return redirect('datosMusico', pk=post.pk)
    else:
        form = MusicoForm()
    return render(request, "practica_08/musico_add.html", {'form': form})

#-------------------Editar cada objeto--------------------------------------------------------
def editGrupo(request, pk):
    post = get_object_or_404(Grupo, pk=str(pk))

    if request.method == 'POST':
        form = GrupoForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()

            return redirect('datosGrupo', pk=post.pk)
    else:
        form = GrupoForm(instance=post)

    return render(request, "practica_08/grupo_edit.html", {'form': form})

def editAlbum(request, pk):
    post = get_object_or_404(Album, pk=str(pk))

    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()

            return redirect('datosAlbum', pk=post.pk)
    else:
        form = AlbumForm(instance=post)

    return render(request, "practica_08/album_edit.html", {'form': form})


def editMusico(request, pk):
    post = get_object_or_404(Musico, pk=str(pk))

    if request.method == 'POST':
        form = MusicoForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()

            return redirect('datosMusico', pk=post.pk)
    else:
        form = MusicoForm(instance=post)

    return render(request, "practica_08/musico_edit.html", {'form': form})


#-------------Mostrar datos de cada objeto----------------------------------------------------
def datosGrupo(request, pk):
    post = get_object_or_404(Grupo, pk=str(pk))
    
    return render(request, "practica_08/datos_grupo.html", {'post': post})

def datosAlbum(request, pk):
    post = get_object_or_404(Album, pk=str(pk))
    
    return render(request, "practica_08/datos_album.html", {'post': post})

def datosMusico(request, pk):
    post = get_object_or_404(Musico, pk=str(pk))
    grupos = post.grupos.all()

    return render(request, "practica_08/datos_musico.html", {'post': post, 'grupos': grupos})

#------------Listar todas las instancias de cada objeto--------------------------------------
def listarGrupos(request):
    grupos = []
    g = Grupo()

    grupos = g.__class__.objects.all()

    return render(request, "practica_08/paginador.html", {'tipo': "Grupo", 'grupos': grupos})

def listarAlbumes(request):
    albumes = []
    a = Album()

    #albumes = a.__class__.objects.all()

    return render(request, "practica_08/paginador.html", {'tipo': "Album"})

def listarMusicos(request):
    musicos = []
    
    m = Musico()

    #musicos = m.__class__.objects.all()

    return render(request, "practica_08/paginador.html", {'tipo': "Musico"})

def reclamaDatos(request):
    print("EMPIEZA RECLAMADATOS")

    tipo = str(request.GET['clase'])

    data = dict()

    ini = request.GET['inicio']
    ini = int(ini)
    print("ini = " + str(ini))
    if tipo == "Grupo":
        
        grupos = []
        
        g = Grupo()

        grupos = g.__class__.objects.all()

        data["len"] = len(grupos)
        i = 0
        for grupo in grupos:
            if i >= ini and i < ini+3:
                print("i = " + str(i))
                print("nombre = " + grupo.nombre)
                data[i]=grupo.nombre
                data[i] = dict()
                data[i]["pk"] = grupo.pk
            i = i+1
        
        
        return JsonResponse(data)
    elif tipo == "Album":
        albumes = []
        a = Album()

        albumes = a.__class__.objects.all()

        data["len"] = len(albumes)
        
        i = 0
        for album in albumes:
            if i >= ini and i < ini+3:
                print("i = " + str(i))
                print("nombre = " + album.titulo)
                data[i]=album.titulo
                data[i] = dict()
                data[i]["pk"] = album.pk
            i = i+1
        return JsonResponse(data)
    else:
        musicos = []
        m = Musico()

        musicos = m.__class__.objects.all()
        data["len"] = len(musicos)

        i = 0
        for musico in musicos:
            if i >= ini and i < ini+3:
                print("i = " + str(i))
                print("nombre = " + musico.nombre)
                data[i]=musico.nombre
                data[i] = dict()
                data[i]["pk"] = musico.pk
                data[i]["nombre"] = musico.nombre + " " + musico.apellidos
            i = i+1
        return JsonResponse(data)

#--------------------Estadísticas------------------------------------------------------------
def cantidades(request):
    g = Grupo()
    grupos = g.__class__.objects.all()

    a = Album()
    albumes = a.__class__.objects.all()

    m = Musico()
    musicos = m.__class__.objects.all()

    data = dict()
    data[0] = len(grupos)
    data[1] = len(albumes)
    data[2] = len(musicos)

    return JsonResponse(data)

def albumes_grupo(request):
    g = Grupo()
    grupos = g.__class__.objects.all()

    a = Album()
    albumes = a.__class__.objects.all()

    data = dict()
    lista = []

    i = 0
    cont = 0

    for grupo in grupos:
        data[i] = dict()
        data[i]["grupo"] = grupo.nombre

        for album in albumes:
            if album.grupo.nombre == grupo.nombre:
                cont = int(cont) + 1
                print("Álbum: " + album.titulo)
                print("Grupo al que pertenece: " + grupo.nombre)

        data[i]["albumes"] = cont
        print("NUMERO DE ALBUMES: " + str(cont))
        cont = 0
        i = int(i) + 1

    data["len"] = len(data)
    print("LONGITUD: ", data["len"])

    return JsonResponse(data)

#-------------Mostrar datos de cada objeto----------------------------------------------------
def borrarGrupo(request, pk):
    post = get_object_or_404(Grupo, pk=str(pk))

    post.delete()
    return redirect('music')

def borrarAlbum(request, pk):
    post = get_object_or_404(Album, pk=str(pk))

    post.delete()
    return redirect('music')

def borrarMusico(request, pk):
    post = get_object_or_404(Musico, pk=str(pk))

    post.delete()
    return redirect('music')

    #return render(request, "practica_08/borrar_grupo.html", {"post": post})

#-----------Registrar, logear y deslogear usuarios-------------------------------------------
def signup(request):
    return render(request, "account/signup.html")
    #if request.method == 'POST':
        #user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        #user.save()

    #    return render(request, "practica_08/music.html")
    #else:
    #    return render(request, "account/signup.html", {'formularios': True})

def login(request):
    return render(request, "account/login.html")
    #if request.method == 'POST':
    #    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    #return render(request, "practica_08/music.html")
    #else:
    #    return render(request, "account/login.html", {'formularios': True})

def logout_view(request):
    logout(request)
    return redirect('music')