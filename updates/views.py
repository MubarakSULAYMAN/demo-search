from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {'name': 'Mubarak'})

def index(request):
    dest1 = Destination()
    dest1.name = "Camelot"
    dest1.img = "destination_1.jpg"
    dest1.desc = "The abandoned city no one knows still exists."
    dest1.price = "590"
    dest1.offer = True

    dest2 = Destination()
    dest2.name = "Thanos"
    dest2.img = "destination_2.jpg"
    dest2.desc = "The inevitable one."
    dest2.price = "690"
    dest2.offer = False
    
    dest3 = Destination()
    dest3.name = "Asgard"
    dest3.img = "destination_3.jpg"
    dest3.desc = "The people is the city."
    dest3.price = "790"
    dest3.offer = False

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'posts': dests})

# def add(request):

#     val1 = int(request.POST["num1"])
#     val2 = int(request.POST["num2"])
#     res = val1 + val2
    
#     return render(request, 'add.html', {'x': val1, 'y': val2, 'result': res})