from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .utils import searchProjects , paginateProjects

from .models import project, Tag
from .forms import ProjectForm, ReviewForm



def projects (request):

    projects, search_query = searchProjects(request)
    custom_range, projects = paginateProjects(request, projects, 3)

    context= { 'projects': projects , 'search_query' : search_query, 'custom_range':custom_range }

    return render(request,'projects/projects.html', context)

def Project (request, pk):
    projectObj = project.objects.get(id=pk)
    form =ReviewForm()

    if request.method =='POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()

        projectObj.getVoteCount
        
        messages.success(request, 'Your review was successfully submitted')
        return redirect('project', pk=projectObj.id)


    return render(request,'projects/single-project.html', {'project': projectObj, 'form':form})

@login_required(login_url="login")
def createProject(request):
    profile= request.user.profile

    form = ProjectForm()

    if request.method == 'POST': 
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid :
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request, 'project was created successfully')
            return redirect('account')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url="login")
def updateProject(request, pk):
    profile= request.user.profile
    Project = profile.project_set.get(id = pk)
    form = ProjectForm(instance= Project)

    if request.method == 'POST': 
        form = ProjectForm(request.POST,  request.FILES, instance= Project)
        if form.is_valid :
            form.save()
            messages.success(request, 'project was updated successfully')
            return redirect('account')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)



@login_required(login_url="login")
def deleteProject(request, pk):
    profile= request.user.profile
    Project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        Project.delete()
        messages.success(request, 'project was deleted successfully')
        return redirect('account') 
    context = {'object': Project}
    return render (request, "delete-template.html", context)
# Create your views here.
