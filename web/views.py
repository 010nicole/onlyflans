from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def indice(req):
    context = {
        "message": "INDICE",
         "user": {"username": "Toto", "password": 1234, "is_active": False},
        "productos": [{"name": "flan de queso", "url":"https://cdn.elcocinerocasero.com/imagen/receta/1000/2018-07-20-09-33-17/flan-de-queso.jpeg"},{"name": "flan de chocolate", "url":"https://cdn.elcocinerocasero.com/imagen/receta/1000/2017-05-08-10-28-01/flan-de-cafe.jpeg"},{"name": "flan de huevo", "url":"https://cdn.elcocinerocasero.com/imagen/receta/1000/2017-03-06-11-47-31/flan-de-huevo.jpeg"},{"name": "flan de vainilla", "url":"https://cdn.elcocinerocasero.com/imagen/receta/1000/2024-01-20-11-27-42/flan-de-leche-condensada.jpeg"},{"name": "flan de galleta", "url":"https://cdn.elcocinerocasero.com/imagen/receta/1000/2022-11-17-21-14-21/flan-de-turron.jpeg"}]
    }
    return render(req, 'index.html', context)

def acerca(req):
    return render(req, 'about.html', {})
# render -> template
def bienvenido(req):
     return render(req, 'welcome.html', {})
