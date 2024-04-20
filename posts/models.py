from django.db import models


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    image = models.URLField(max_length=200)
    author = models.CharField(max_length=50)
    
    def __str__(self):
        return self.titulo