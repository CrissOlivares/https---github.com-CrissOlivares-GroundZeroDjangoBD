from django.urls import path
from . import views
from django.contrib import admin
urlpatterns=[
    path('',views.GroundZeroInicio,name="GroundZeroInicio.html"),
    path('GorundZeroCompra.html',views.GorundZeroCompra,name="GorundZeroCompra.html"),
    path('GroundZeroArtistas.html',views.GroundZeroArtistas,name="GroundZeroArtistas.html"),
    path('GroundZeroCuadros.html',views.GroundZeroCuadros,name="GroundZeroCuadros.html"),
    path('GroundZeroEsculturas.html',views.GroundZeroEsculturas,name="GroundZeroEsculturas.html"),
    path('GroundZeroOrfebreria.html',views.GroundZeroOrfebreria,name="GroundZeroOrfebreria.html"),
    path('GroundZeroLogin.html',views.GroundZeroLogin,name="GroundZeroLogin.html"),
    path('GroundZeroRegister.html',views.GroundZeroRegister,name="GroundZeroRegister.html"),
    path('GroundZeroPaises.html',views.GroundZeroPaises,name="GroundZeroPaises.html"),
    path('GroundZeropPQ.html',views.GroundZeropPQ,name="GroundZeropPQ.html"),
    path('index.html',views.index,name="index.html"),
    path('lista_tarjetas.html',views.lista_tarjetas,name="lista_tarjetas.html"),
    path('editar_tarjeta/<int:tarjeta_id>/', views.editar_tarjeta, name='editar_tarjeta'),
    path('eliminar_tarjeta/<int:tarjeta_id>/', views.eliminar_tarjeta, name='eliminar_tarjeta'),
    path('success/', views.success, name='success'),
    path('menu.html',views.menu, name='menu.html'),
   path('login/', views.login_view, name='login'),

]
