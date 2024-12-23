from rest_framework import  serializers
from .models import *
from django.contrib.auth.models import User

class blogSerializers(serializers.ModelSerializer):
     class Meta:
         model = Blog
         fields = ['id','title','content','created_at']
         fields = '__all__'

class UserSeriliazers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username','password','email']
    def create(self, validated_data):
        user= User.objects.create_user(**validated_data)
        return user


