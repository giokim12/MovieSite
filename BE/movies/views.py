from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie, Genre, Credit
from .serializers import MovieListSerializer, ActorSerializer
# Create your views here.


@api_view(['GET'])
def movie_list_voted(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        voted_movies = []
        for movie in movies:
            if movie.vote_avg > 5:
                voted_movies.append(movie)
        # print(new_movies[0].vote_avg)
        voted_movies = sorted(voted_movies, key=lambda x: -x.vote_avg)
        voted_movies10 = voted_movies[:6]
        serializer = MovieListSerializer(voted_movies10, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def movie_list_old(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        old_movies = []
        for movie in movies:
            if movie.vote_avg > 5:
                old_movies.append(movie)
        # print(new_movies[0].vote_avg)
        old_movies = sorted(old_movies, key=lambda x: x.released_date)
        old_movies10 = old_movies[:6]
        serializer = MovieListSerializer(old_movies10, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def movie_list_popular(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        popular_movies = []
        for movie in movies:
            if movie.vote_avg > 5:
                popular_movies.append(movie)
        # print(new_movies[0].vote_avg)
        popular_movies = sorted(popular_movies, key=lambda x: -x.popularity)
        popular_movies10 = popular_movies[:6]
        serializer = MovieListSerializer(popular_movies10, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def actor_list(request):
    if request.method == 'GET':
        actors = get_list_or_404(Credit)
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)
