from django.shortcuts import render
from rest_framework import generics
from dateen.serializers import CategorySerializer,FeaturedArticleSerializer 

from dateen.models import Category, FeaturedArticle


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class FeaturedArticleListView(generics.ListAPIView):
    queryset = FeaturedArticle.objects.all()
    serializer_class = FeaturedArticleSerializer
