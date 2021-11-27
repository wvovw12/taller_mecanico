from django.urls import path, include
from .views import home, listaServicios

urlpatterns = [
    path('',home,name='home'),
    path('listaServicios/',listaServicios, name='listaServicios')
]