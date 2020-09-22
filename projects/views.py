from django.shortcuts import render, get_object_or_404
from .models import Project

def allProjects(request):
    projects = Project.objects
    return render(request, 'projects/projects.html', {'projects': projects})

def projectDetail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/projectdetail.html', {'project': project})
