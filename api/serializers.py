from rest_framework import serializers
from projects.models import project,Tag,review
from users.models import Profile


class Reviewserializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = '__all__'

class Profileserializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class Tagserializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class Projectserializer(serializers.ModelSerializer):
    owner = Profileserializer(many=False)
    tag = Tagserializer(many=True)
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = project
        fields= '__all__'
        

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializers = Reviewserializer(reviews, many=True)
        return serializers.data 
