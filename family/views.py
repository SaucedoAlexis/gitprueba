from django.shortcuts import render

from family.models import Family


# Create your views here.

def listar_familia(request):
    family = Family.objects.all()
    return render(request, "Datos_Familia.html",{"familia": Family})