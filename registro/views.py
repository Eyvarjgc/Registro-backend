from django.shortcuts import render,redirect
from .models import categorias,datos,Message,User
from .form import Categorias_Form,datosform,RegisterUser,Image
from django.template import context,Template
from django.http import HttpRequest,HttpResponseRedirect
from .form import Categorias_Form
from django.db.models import Q
# from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    host = User.objects.all()
    search = request.GET.get('search') if request.GET.get('search') != None else ""
    objetos = datos.objects.filter( Q(categorie__name__icontains = search)|
        Q(name__icontains = search))
    categoria = categorias.objects.all()
    categorieCount = categoria.count()
    return render(request,'registro/home.html',{'categoria':categoria,'objetos':objetos,'count':categorieCount,'host':host})

def objeto(request,categorie):
    dato = datos.objects.filter(categorie = categorie)
    # context = {'dato':dato,'count':listCount}
    listCount = dato.count()
    return render(request,'registro/objetos.html',{'dato':dato,'count':listCount})

@login_required
def add_categoria(request):
    form = Categorias_Form()
    if request.method == 'POST':
        form = Categorias_Form(request.POST or None)
        if form.is_valid():
            c = categorias.objects.create(**form.cleaned_data)
            c.save()
            return redirect('home')
        
    return render(request,'registro/add_categoria.html',{'form':form})

@login_required
def add_datos(request):
    add = datosform()
    if request.method == 'POST':
        add = datosform(request.POST or None)
        if add.is_valid():
            add.save()
            return redirect('home')
    return render(request,'registro/add_datos.html',{'form':add})

def edit(request,pk):
    dato = datos.objects.get(id = pk)
    editar = datosform(instance=dato)
    if request.method == 'POST':
        editar = datosform(request.POST, instance=dato)
        if editar.is_valid():
            editar.save()
            return redirect('home')
        
    return render(request,'registro/add_datos.html',{'form':editar})

def delete(request,pk):
    dato = datos.objects.get(id=pk)
    if request.method == 'POST':
        dato.delete()
        return redirect('home')
    return render(request,'registro/delete.html',{'obj':dato})

def conver(request,pk):
    dato = datos.objects.get(id= pk)
    datoMessages = dato.message_set.all().order_by('-created')
    participantes = dato.participantes.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = dato,
            body = request.POST.get('body')
        )
        dato.participantes.add(request.user)
        return redirect('conver', pk=dato.id)

    context = {'dato':dato,'messages':datoMessages,'participantes':participantes}
    return render(request,'registro/messages.html',context)


def deletemessage(request,pk):
    message = Message.objects.get(id = pk)
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request,'registro/delete.html',{'obj':message})

@login_required
def logRegis(request):
    return render(request,'registration/login.html')


# def logRegis(request):
#     username = ""
#     password = ""
#     if request.user.is_authenticated:
#         return redirect('home')
#     if request.method == 'POST':
#         username = request.POST.get('username').lower
#         password = request.POST.get('password')    
#         try:
#             user = User.objects.get(username = username)
#         except User.DoesNotExist:
#             messages.error(request,'Este nombre de usuario ya esta en uso')
            
#         user = authenticate(request, username = username, password = password)
#         if user is not None:
#             login(request,user)
#             return redirect('home')
#         else:
#             messages.error(request,'usuario o contraseña incorrecta')

#     form = RegisterUser()
#     return render(request,'registro/log_regis.html',{'form':form})

def logoutUser(request):
    logout(request)
    return redirect('home')

def register(request):
        form = RegisterUser()
        if request.method == 'POST':
            form = RegisterUser(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                login(request,user)
                return redirect('home')
            
            else:
                messages.error(request,'no ha ingresado las contraseñas correctamente')
        context = {'form':form}
        return render(request,'registro/register.html',context)

# def ver(request):
#     datoall = datos.objects.all()
#     if request.method == 'POST':
#         if request.POST.get('save'):
#             for objeto in datoall.name.all():
#                 if request.POST.get('c' + str(objeto.id)) == 'clicked':
#                     objeto.done == True
#                 else:
#                     objeto.done == False
#                 objeto.save()
                
#     return render(request,'registro/ver.html',{'dato':datoall})

def ver(request):
    datoall = datos.objects.all()
    if request.method == 'POST':
        form = datosform(request.POST or None)
        if form.is_valid():
            objeto.save()
                
    return render(request,'registro/ver.html',{'dato':datoall})


def imagen(request):
    image = Image()
    if request.method == 'POST':
        image = Image(request.POST or None)
        if image.is_valid():
            image.save()
        
    return render(request,'registro/imagen.html',{'image':image})


