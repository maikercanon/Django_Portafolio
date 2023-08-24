from django.shortcuts import render
from .models import Project
# Create your views here.d

def home(request):
    mis_proyectos= Project.objects.all()
    return render(request, 'home.html',{'proyectos':mis_proyectos})



#42:28 reanudar video