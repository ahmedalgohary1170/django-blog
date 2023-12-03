#form
from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model =User
        fields=['id','username','email']




class Postserializer(serializers.ModelSerializer):
    author=UserSerializers()
    category=serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = '__all__'
