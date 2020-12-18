from django.shortcuts import render, redirect
from .models import *
from .decorators import sinIdentificar, permitirUsuarios
from .forms import ClienteForm, CrearUsuarioForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def base_layout(request):
    template = 'tienda/main.html'
    return render(request, template)


@login_required(login_url='login')
@permitirUsuarios(allowed_roles=['admin', 'usuarios'])
def home(request):
    return render(request, 'tienda/index.html')


@login_required(login_url='login')
@permitirUsuarios(allowed_roles=['admin', 'usuarios'])
def productos(request):
    producto = Producto.objects.all()
    cliente = Cliente.objects.all()
    context = {'producto': producto, 'cliente': cliente}
    return render(request, 'tienda/productos.html', context)


@login_required(login_url='login')
@permitirUsuarios(allowed_roles=['admin', 'usuarios'])
def contacto(request):
    return render(request, 'tienda/contactanos.html')


@login_required(login_url='login')
@permitirUsuarios(allowed_roles=['admin'])
def cliente(request, pk):
    cliente = Cliente.objects.get(id=pk)
    context = {'cliente': cliente}
    return render(request, 'tienda/Clientes.html', context)


@login_required(login_url='login')
@permitirUsuarios(allowed_roles=['admin'])
def crearCliente(request):
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'tienda/clienteF.html', context)


@login_required(login_url='login')
@permitirUsuarios(allowed_roles=['admin'])
def actualizarCliente(request, pk):
    cliente = Cliente.objects.get(id=pk)
    form = ClienteForm(instance=cliente)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'tienda/clienteF.html', context)


@login_required(login_url='login')
@permitirUsuarios(allowed_roles=['admin'])
def borrarCliente(request, pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method == "POST":
        cliente.delete()
    context = {'item': cliente}
    return render(request, 'tienda/borrar.html', context)

@sinIdentificar
def paginaRegistro(request):
    form = CrearUsuarioForm()
    if request.method == "POST":
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'tienda/registro.html', context)


@sinIdentificar
def paginaLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    context = {}
    return render(request, 'tienda/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
