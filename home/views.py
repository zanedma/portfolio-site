from django.shortcuts import render
from .models import Home
from projects.models import Project
from updates.models import Update

# Create your views here.
def home(request):
    context = {
        'home_vals': Home.objects.get(pk=1),
        'projects': Project.objects,
        'updates': Update.objects.all().order_by('pub_date')[:3]
    }
    return render(request, 'home/home.html', context)
