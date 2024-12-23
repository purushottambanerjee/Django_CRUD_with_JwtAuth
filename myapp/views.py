from django.shortcuts import render
from django.http import  HttpResponse
from rest_framework import status,permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from rest_framework.response import Response

from .models import Blog
from .serializers import blogSerializers,UserSeriliazers

# Create your views here.

class BlogViews(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,req,format = None):

        search_term = req.query_params.get('search',None)
        if(search_term==None):
            blogs = Blog.objects.all()
        else:
            blogs = Blog.objects.filter(title__icontains = search_term)
        serializer = blogSerializers(blogs,many=True)

        return Response(serializer.data)
    def post(self,req,format=None):


        serializer = blogSerializers(data = req.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,req):
        search_id = req.query_params.get('id',None)
        if(search_id!=None):
            try :
                blogs = Blog.objects.filter(id = search_id)
            except:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
            blogs.delete()
            return Response({"detail":"DELETED BLOG WITH ID -"+search_id},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail":"PLEASE PASS the ID in parameter"},status=status.HTTP_400_BAD_REQUEST)

    def put(self, req):
        search_id = req.query_params.get('id', None)
        if (search_id != None):
            try:
                blog = Blog.objects.filter(id = search_id)
                serializer = blogSerializers(data=req.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"detail":"PLEASE PASS the ID in parameter"},status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    def post(self,req):
        permission_classes = [permissions.AllowAny]  # Allow any user to register
        seriliazer = UserSeriliazers(data=req.data)
        if seriliazer.is_valid():
            user = seriliazer.save()
            return Response({
                "message" : "User has been Created"
            },status.HTTP_201_CREATED)
        return (seriliazer.errors,status.HTTP_400_BAD_REQUEST)



