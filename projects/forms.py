from django.forms import ModelForm
from .models import project

class ProjectForm(ModelForm):
    class Meta:
        model = project 
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tag' ]

