from django.shortcuts import render
from django.http import HttpResponse
from api.models import Glass


# Create your views here.
def myHomeView(request, *args, **kwargs): 
    '''
    *N° variables indeterminados de argumentos
    **Recibir argumentos que pueden ser iterados
    '''
    vidrios = Glass.objects.all()
    data = {
        'vidrios': vidrios
    }
    return render(request, 'home.html', data)

def myGlass(request, myID): 
    obj = Glass.objects.get(id = myID)
    context = {
        "objeto": obj,
    }
    return render(request, 'Glass.html', context)