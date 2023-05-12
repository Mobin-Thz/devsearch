from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects , name="projects"),
    path('project-obj/<str:pk>', views.Project , name="project"),

    path('create-project/', views.createProject, name="create-project")
]