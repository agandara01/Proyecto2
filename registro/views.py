from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona
from django.shortcuts import redirect
# Create your views here.

#importar user
from django.contrib.auth.models import User
#sistema de autenticación 
from django.contrib.auth import authenticate,logout, login as auth_login

from django.contrib.auth.decorators import login_required



def formulario(request):
    usuario = request.session.get('usuario',None)
    return render(request,'formulario.html',{'name':'Registro de personas','personas':Persona.objects.all(),'usuario':usuario})

def inicio(request):
    return render(request,'inicio.html',{})


def crear(request):
    nombre = request.POST.get('nombre','')
    correo = request.POST.get('correo','')
    contrasenia = request.POST.get('contrasenia','')
    foto = request.FILES.get('foto',False)
    persona = Persona(nombre=nombre,correo=correo,contrasenia=contrasenia,foto = foto)
    persona.save()
    return redirect('formulario')

@login_required(login_url='login')
def eliminar(request,id):
    persona = Persona.objects.get(pk = id)
    persona.delete()
    return redirect('formulario')

@login_required(login_url='login')
def editar(request):
    nombre = request.POST.get('nombre','')
    correo = request.POST.get('correo','')
    id = request.POST.get('id',0)
    persona = Persona.objects.get(pk = id)
    persona.nombre = nombre
    persona.correo = correo
    persona.save()
    return redirect('formulario')

@login_required(login_url='login')
def cerrar_session(request):
    del request.session['usuario']
    logout(request)
    return redirect('formulario')

def login(request):
    return render(request,'login.html',{})

def login_iniciar(request):
    usuario = request.POST.get('nombre_usuario','')
    contrasenia = request.POST.get('contrasenia','')
    user = authenticate(request,username=usuario, password=contrasenia)

    if user is not None:
        auth_login(request, user)
        request.session['usuario'] = user.first_name+" "+user.last_name
        return redirect("formulario")
    else:
        return redirect("login")
    