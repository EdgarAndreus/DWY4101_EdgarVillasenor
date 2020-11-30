from django.urls import path
from . import views


urlpatterns = [
    path('registro/', views.paginaRegistro, name='paginaRegistro'),
    path('login/', views.paginaLogin, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('productos/', views.productos, name='productos'),
    path('contactanos/', views.contacto, name='contacto'),
    path('clientes/<str:pk>/', views.cliente, name='cliente'),
    path('crearCliente/', views.crearCliente, name='crearCliente'),
    path('actualizarCliente/<str:pk>/', views.actualizarCliente, name='actualizarCliente'),
    path('borrarCliente/<str:pk>/', views.borrarCliente, name='borrarCliente'),


]

