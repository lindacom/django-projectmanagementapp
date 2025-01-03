from django.db import models

from embed_video.fields import EmbedVideoField

# Create your models here.

class Video (models.Model):
    title = models.CharField(max_length = 100)
    added = models.DateTimeField(auto_now_add = True)
    url = EmbedVideoField()

    def __str__ (self):
        return str(self.title)

    class Meta:
        ordering = ['-added']

class Article (models.Model):
    title = models.CharField(max_length = 100)
    added = models.DateTimeField(auto_now_add = True)
    url = models.CharField(max_length = 100)

    def __str__ (self):
        return str(self.title)

    class Meta:
        ordering = ['-added']
