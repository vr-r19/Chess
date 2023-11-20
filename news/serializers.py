from rest_framework import serializers
from news.models import News, BookAuthor, TopKitoblar, SearchNews

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = '__all__'

