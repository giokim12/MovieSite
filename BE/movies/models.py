from django.db import models

# Create your models here.


class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    popularity = models.IntegerField()
    vote_avg = models.IntegerField()
    overview = models.TextField()
    released_date = models.DateField()
    poster_path = models.TextField(null=True)
    genres = models.ManyToManyField(Genre, related_name='movies')
