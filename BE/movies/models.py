from django.db import models

# Create your models here.


class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

class Actor(models.Model):
    actor_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.IntegerField()
    popularity = models.IntegerField()
    profile_path = models.TextField(null=True)


class Movie(models.Model):
    # auto_increment_id = models.AutoField(primary_key = True)
    # movie_id = models.ForeignKey(Credit, on_delete=models.CASCADE)
    movie_id = models.IntegerField(primary_key = True)
    title = models.CharField(max_length=100)
    popularity = models.IntegerField()
    vote_avg = models.IntegerField()
    overview = models.TextField()
    released_date = models.DateField()
    poster_path = models.TextField(null=True)
    genres = models.ManyToManyField(Genre, related_name='genre_contained_movies')
    # movie_credits = models.ManyToManyField(Credit, related_name='genre_contained_movies')
    
    
class Credit(models.Model):
    # movie_id = models.IntegerField(primary_key = True)
    auto_increment_id = models.AutoField(primary_key=True)
    person_id = models.IntegerField()
    # person_id = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie= models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    popularity = models.IntegerField()
    character = models.CharField(max_length=100)
    profile_path = models.TextField(null=True)
    credit_movies = models.ManyToManyField(Movie, related_name='movie_contained_credits')