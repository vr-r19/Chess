from django.db import models

class News(models.Model):
    image=models.ImageFiel(upload_to='news')
    date_published=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=50)
    description=models.TextField()
    twitter_url=models.URLField()
    facebook_url=models.URLField()
    telegram_url=models.URLField()
    view_count=models.IntegerField()  # view countni ishlaydigan qilish kerak
    def __str__(self):
        return self.title
    
