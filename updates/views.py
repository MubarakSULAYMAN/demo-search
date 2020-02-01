from django.shortcuts import render
from .models import InfoUpdate

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {'name': 'Mubarak'})

def index(request):

    dests = InfoUpdate.objects.all()
    
    return render(request, 'index.html', {'posts': dests})
