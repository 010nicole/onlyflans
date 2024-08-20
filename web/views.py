from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan, ContactForm, Profile
from .forms import ContactFormForm, ProfileForm, UserForm
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

def detalle_flan(req,flan_uuid):
    flan = Flan.objects.get(flan_uuid = flan_uuid)
    return render(req, 'detail_flan.html',{'flan':flan})

@login_required
def profile_view(req):
    user_id = req.user.id
    #profile = Profile.objects.get(user_id=user_id)
    user = req.user
    if not hasattr(user,'profile'):
        Profile.objects.create(user=user) # crea tabla con datos vacios

    if req.method == 'POST':
        user_form = UserForm(req.Post, instance=req.user)
        profile_form = ProfileForm(req.POST, instance=req.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/profile_exito')
    else: 
        user_form = UserForm(instance=req.user)
        profile_form =ProfileForm(instance=req.user.profile)
    return  render(req,'profile.html',{'user_form':user_form,'profile_form':profile_form})

def profile_exito(req):
    return render(req,'profile_exito.html',{})
            
        
 
    
    