from django.shortcuts import render
from rest_framework import generics
from notebook.serializers import CategorySerializer,AuthorSerializer,BlogPostSerializer
from notebook.models import Category,Author,BlogPost

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
class BlogPostListView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer