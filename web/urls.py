from django.urls import path
from . import views 

urlpatterns = [
    path('', views.indice),
    path('acerca/', views.acerca),
    path('bienvenido/', views.bienvenido),
]