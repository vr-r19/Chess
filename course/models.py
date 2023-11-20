from django.db import models

DARAJA=(
      ("Boshlang'ich", "Boshlang'ich"), 
    ("O'rta", "O'rta"), 
    ("Qiyin", "Qiyin"), 
)
LANGUAGE=(
    ("Uz", "Uz"),
    ("Rus", "Rus"),
    ("Eng", "Eng"),
)



class LessonCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class VideoLesson(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    discount=models.IntegerField(default='')
    price=models.IntegerField()
    daraja=models.CharField(max_length=50, choices=DARAJA, default='Boshlangich')  
    language=models.CharField(max_length=50, choices=LANGUAGE, default='Uz')
    rating=models.FloatField()
    categories = models.ManyToManyField(LessonCategory)
    def __str__(self):
        return self.name
