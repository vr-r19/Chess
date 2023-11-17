from rest_framework import serializers
from dateen.models import Category, User, FeaturedArticle


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title','image')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class FeaturedArticleSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    user=UserSerializer()
    class Meta:
        model = FeaturedArticle
        fields = "__all__"