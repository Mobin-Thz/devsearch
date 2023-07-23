from django.contrib import admin

# Register your models here.
from .models import project , review , Tag

admin.site.register(project)
admin.site.register(review)
admin.site.register(Tag)