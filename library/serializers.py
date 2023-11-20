from rest_framework import serializers
from .models import BookAuthor, TopBooks, BookCategory, Book



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = ('name',)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'