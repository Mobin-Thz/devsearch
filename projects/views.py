from django.shortcuts import render
from django.http import HttpResponse
from .models import project
projectslist = [
            {
            'id':'1',
            'title': 'Ecommerce website',
            'description':'Fully functional ecommerce website'
            },
            {
            'id':'2',
            'title': 'Portfolio Website',
            'description':'This was a project where i built out my portfolio'
            },
            {
            'id':'3',
            'title': 'Social Network',
            'description':'Awesome open source project i am still working on'
            },
]


def projects (request):

    projects = project.objects.all()
    context= { 'projects': projects }

    return render(request,'projects/projects.html', context)

def Project (request, pk):
    projectObj = project.objects.get(id=pk)
    return render(request,'projects/single-project.html', {'project': projectObj})


# Create your views here.
