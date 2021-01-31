from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('<em>Primera vista</em>')


def index2(request):
    contexts = {
        'index_var': {'1': 'PRUEBA'},
        'comment_var': 'PRUEBA2',
        'usuario_var': 'NombreUsuario',
        'likes': '500 me gusta',
        'caption': 'Cogito ergo sum'
    }
    return render(request, 'AppTwo\\index.html', contexts)


def index3(request):
    contexts = {
        'nombreUsuario_var': 'NombreUsuario',
        'contraseña_var': '',
        'index_var': {'1': 'PRUEBA'},
        'comment_var': 'PRUEBA2',
        'usuario_var': 'NombreUsuario'
    }
    return render(request, 'AppTwo\\registro.html', contexts)
def index4(request):
    contexts = {
        'nombreUsuario_var': 'NombreUsuario',
        'contraseña_var': '',
        'index_var': {'1': 'PRUEBA'},
        'comment_var': 'PRUEBA2',
        'usuario_var': 'NombreUsuario'
    }
    return render(request, 'AppTwo\\login.html', contexts)

def index5(request):
    contexts = {
        'nombreUsuario_var': 'NombreUsuario',
        'contraseña_var': '',
        'index_var': {'1': 'PRUEBA'},
        'comment_var': 'PRUEBA2',
        'usuario_var': 'NombreUsuario'
    }
    return render(request, 'AppTwo\\cabecera.html', contexts)

def index6(request):
    contexts = {
        'nombreUsuario_var': 'NombreUsuario',
        'contraseña_var': '',
        'index_var': {'1': 'PRUEBA'},
        'comment_var': 'PRUEBA2',
        'usuario_var': 'NombreUsuario',
        'usuario2_var': 'NombreUsuario2',
        'mensaje1': 'Hola bb',
        'mensaje2': 'Holaaaaaaa'
    }
    return render(request, 'AppTwo\\chatPrivado.html', contexts)

def index7(request):
    contexts = {
        'nombreUsuario_var': 'NombreUsuario',
        'contraseña_var': '',
        'index_var': {'1': 'PRUEBA'},
        'comment_var': 'PRUEBA2',
        'usuario_var': 'NombreUsuario'
    }
    return render(request, 'AppTwo\\configuracion.html', contexts)

def index8(request):
    contexts = {
        'nombreUsuario_var': 'NombreUsuario',
        'contraseña_var': '',
        'index_var': {'1': 'PRUEBA'},
        'comment_var': 'PRUEBA2',
        'usuario_var': 'NombreUsuario',
        'descripcion': 'Texto de prueba 4'
    }
    return render(request, 'AppTwo\\informacion.html', contexts)

def index9(request):
    contexts = {
        'nombreUsuario_var': 'NombreUsuario',
        'contraseña_var': '',
        'index_var': {'1': 'PRUEBA'},
        'comment_var': 'PRUEBA2',
        'usuario_var': 'NombreUsuario'
    }
    return render(request, 'AppTwo\\publicacion.html', contexts)

