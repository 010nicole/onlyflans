from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def acerca(req):
    return render(req, 'about.html', {})
# render -> template
