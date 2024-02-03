from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    imgPath = models.CharField(max_length=255)
    duration = models.IntegerField()
    genre = models.JSONField()
    language = models.CharField(max_length=255)
    mpaaRatingType = models.CharField(max_length=10)
    mpaaRatingLabel = models.CharField(max_length=255)
    userRating = models.CharField(max_length=1)