from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Curso

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cursosListados = Curso.objects.all()
    return render(request, "gestionCursos.html", {"cursos": cursosListados})

def registrarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']
    
    curso=Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect('/')

def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso":curso})

def editarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']
    
    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    
    return redirect('/')

def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('protected_view')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'login.html')

def protected_view(request):
    return render(request, 'protected.html')
def index(request):
    return render(request, 'index.html')

