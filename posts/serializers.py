#form
from rest_framework import serializers
from .models import Post

class Postserializer(serializers.ModelSerializer):
    author=serializers.StringRelatedField()
    category=serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = '__all__'
