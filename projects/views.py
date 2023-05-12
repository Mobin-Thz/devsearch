from django.shortcuts import render
from django.http import HttpResponse
from .models import project
from .forms import ProjectForm

def projects (request):

    projects = project.objects.all()
    context= { 'projects': projects }

    return render(request,'projects/projects.html', context)

def Project (request, pk):
    projectObj = project.objects.get(id=pk)
    return render(request,'projects/single-project.html', {'project': projectObj})

def createProject(request):
    form = ProjectForm()
    context = {'form': form}
    return render(request, "projects/project_form.html", context)

# Create your views here.
