from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes),
    path('projects/', views.getprojects),
    path('projects/<str:pk>/', views.getproject),
]