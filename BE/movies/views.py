from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie, Genre, Credit
from .serializers import MovieListSerializer, ActorSerializer
# Create your views here.


@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        new_movies = []
        for movie in movies:
            if movie.vote_avg > 5:
                new_movies.append(movie)
        # print(new_movies[0].vote_avg)
        new_movies = sorted(new_movies, key=lambda x: -x.vote_avg)
        new_movies10 = new_movies[:10]
        serializer = MovieListSerializer(new_movies10, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def movie_list_2(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        new_movies = []
        for movie in movies:
            if movie.vote_avg > 5:
                new_movies.append(movie)
        # print(new_movies[0].vote_avg)
        new_movies = sorted(new_movies, key=lambda x: x.vote_avg)
        new_movies10 = new_movies[:10]
        serializer = MovieListSerializer(new_movies10, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def actor_list(request):
    if request.method == 'GET':
        actors = get_list_or_404(Credit)
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)
