from django.shortcuts import render, redirect
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

    if request.method == 'POST': 
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid :
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)


def updateProject(request, pk):
    
    Project = project.objects.get(id = pk)
    form = ProjectForm(instance= Project)

    if request.method == 'POST': 
        form = ProjectForm(request.POST,  request.FILES, instance= Project)
        if form.is_valid :
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)




def deleteProject(request, pk):
    Project = project.objects.get(id=pk)
    if request.method == 'POST':
        Project.delete()
        return redirect('projects') 
    context = {'object': Project}
    return render (request, "projects/delete-template.html", context)
# Create your views here.
