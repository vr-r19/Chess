from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()
    def __str__(self):
        return self.name
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    image=models.ImageField(upload_to='blogpost')
    def __str__(self):
        return self.title