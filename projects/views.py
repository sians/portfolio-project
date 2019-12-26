from django.shortcuts import render

from .models import Project


def home(request):
    return render(request, 'projects/home.html')

def contact(request):
    return render(request, 'projects/contact.html')

def projects(request):
    projects = Project.objects
    return render(request, 'projects/projects.html', {'projects': projects})

def about(request):
    return render(request, 'projects/about.html')
