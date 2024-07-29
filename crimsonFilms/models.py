from django.db import models

# Create your models here.

class Film(models.Model):
    titleO = models.CharField(max_length=300)
    titleEn = models.CharField(max_length=300)
    titleRu = models.CharField(max_length=300)
    kID = models.IntegerField(default=0)
    imdbID = models.CharField(max_length=30)
    ratingIMDB = models.FloatField(default=0)
    ratingKP = models.FloatField(default=0)
    videoLocal = models.CharField(max_length=1000)
    poster = models.CharField(max_length=1000)
    posterLocal = models.CharField(max_length=1000)


