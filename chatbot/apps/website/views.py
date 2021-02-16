from django.shortcuts import render
from apps.website.models import Comida
# Create your views here.


def index_website(request):
    return render(request, 'base.html')
  
    Comida.objects.create(nombre='Tacos')
    comida_lista = Comida.objects.all()

    for comida in comida_lista:
        print(comida.nombre)

   #tacos = Comida.objects.get(id=1)
   #tacos.nombre = 'tacos de asada'
   #tacos.save()

   #Comida.objects.get(id=1).delete()
   
   

