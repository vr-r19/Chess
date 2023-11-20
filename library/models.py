from django.db import models

import datetime
YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

LEVEL=(
      ("Boshlang'ich", "Boshlang'ich"), 
    ("O'rta", "O'rta"), 
    ("Qiyin", "Qiyin"), 
)
LANGUAGE=(
    ("Uz", "Uz"),
    ("Rus", "Rus"),
    ("Eng", "Eng"),
)
class BookAuthor(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class TopBooks(models.Model):
    image=models.ImageField(upload_to='topkitoblar')
    title=models.CharField(max_length=50)
    author=models.ManyToManyField(BookAuthor)

class BookCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Book(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='kitoblar')
    content_text=models.TextField()
    author=models.CharField(max_length=50)
    discount=models.IntegerField(default='')
    price=models.IntegerField()
    daraja=models.CharField(max_length=50, choices=LEVEL, default='Boshlangich')  
    language=models.CharField(max_length=50, choices=LANGUAGE, default='Uz')
    rating=models.FloatField()
    categories = models.ManyToManyField(BookCategory)
    pages=models.IntegerField()
    date_of_publish=models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)


    def __str__(self):
        return self.name
