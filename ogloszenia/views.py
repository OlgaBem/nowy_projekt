from django.shortcuts import render
from .models import Ogloszenie
from django.shortcuts import redirect

def lista_ogloszen(request):
    ogloszenia = Ogloszenie.objects.all()
    return render(request, 'ogloszenia/lista.html', {'ogloszenia': ogloszenia})



def rezerwuj_ogloszenie(request, id):
    ogloszenie = Ogloszenie.objects.get(id=id)
    ogloszenie.zarezerwowane = True
    ogloszenie.save()
    return redirect('lista_ogloszen')