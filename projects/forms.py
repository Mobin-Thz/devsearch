from typing import Any, Dict, Mapping, Optional, Type, Union
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm , widgets
from django import forms
from django.forms.utils import ErrorList
from .models import project

class ProjectForm(ModelForm):
    class Meta:
        model = project 
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tag' ]

        widgets = {
            'tag' : forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args , **kwargs): 
        super(ProjectForm, self).__init__(*args , **kwargs)

        for name , field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        # self.fields['title'].widget.attrs.update(
        #     {'class': 'input', 'placeholder': 'Add Title' })