# projects/views.py

from django.shortcuts import render
from .models import Project, Category
from django.shortcuts import render, get_object_or_404


def project_index(request):
    projects = Project.objects.all()
    categories = Category.objects.all()
    return render(request, 'projects/project_index.html', {'projects': projects, 'categories': categories})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    related_projects = Project.objects.filter(category=project.category).exclude(id=project.id)[:3]
    return render(request, 'projects/project_detail.html', {'project': project, 'related_projects': related_projects})

