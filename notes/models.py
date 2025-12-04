from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    likes = models.PositiveSmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
