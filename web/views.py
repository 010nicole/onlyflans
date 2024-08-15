from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . models import Flan, ContactForm
from .forms import ContactFormForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def indice(req):
    flanes_publicos = Flan.objects.filter(is_private=False)

    return render(req, 'index.html', {"flanes_publicos":flanes_publicos})

def acerca(req):
    return render(req, 'about.html', {})
# render -> template

@login_required
def bienvenido(req):
    flanes_privados = Flan.objects.filter(is_private=True)

    return render(req, 'welcome.html', {"flanes_privados":flanes_privados})

def contacto(req):
    if req.method == 'POST':
        
        #* FORM
        form = ContactFormForm(req.POST) # <- {"customer_email": "kiki@gamial.com", "customer_name": "Kiki", "message": "Hola soy Kiki"}
        if form.is_valid():
            #* MODEL - Guardamos la data en nuestra DB en la TABLA CONACTFORM
            ContactForm.objects.create(**form.cleaned_data) # pasamos la data del diccionario .cleaned_data a argumentos
            return HttpResponseRedirect('/exito')
    else: 
        form = ContactFormForm()    
    return render(req, 'contacto.html', {'form':form})
    
def exito(req):
    return render(req,'exito.html',{})