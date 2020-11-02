from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.productos, name='productos'),
    path('contactanos/', views.contacto, name='contacto'),

]

urlpatterns += [
    path('producto/crear', views.CrearProducto.as_view(), name='crear'),
    path('producto/<int:pk>/modificar', views.ModificarProducto.as_view(), name='modificar'),
    path('producto/<int:pk>/borrar', views.BorrarProducto.as_view(), name='borrar'),
]