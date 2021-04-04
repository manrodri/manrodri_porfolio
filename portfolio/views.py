from django.shortcuts import render, get_object_or_404
from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})


def resume(request):
    return render(request, 'portfolio/resume.html')


def show_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'portfolio/show_project.html', {'project': project})