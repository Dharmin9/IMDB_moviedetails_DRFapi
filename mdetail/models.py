from django.db import models


class MovieDetail(models.Model):

    name = models.CharField(max_length=100)
    rating = models.CharField(max_length=10)
    release_date = models.CharField(max_length=32)
    duration = models.CharField(max_length=10)
    description = models.TextField()

    class Meta:
        db_table = 'imdbmovie'
