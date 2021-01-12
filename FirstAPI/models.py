from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=200)


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=200)
    tags = models.ManyToManyField(Tag, related_name='posts')
    