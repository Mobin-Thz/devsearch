from rest_framework import serializers
from projects.models import project


class Projectserializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields= '__all__'
        