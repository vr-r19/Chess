from django.db import models

class Category(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='category')
class FeaturedArticle(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    article_image=models.ImageField(upload_to='featured')
    profile_image=models.ImageField(upload_to='featured')
    date_published=models.DateField()
    read_more_link=models.URLField()
class User(models.Model):
    name=models.CharField(max_length=50)
    profile_image=models.ImageField(upload_to='featured')

    