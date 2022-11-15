from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie, Genre
from .serializers import MovieListSerializer
# Create your views here.


@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        new_movies = []
        for movie in movies:
            if movie.vote_avg > 8:
                new_movies.append(movie)
        # print(new_movies[0].vote_avg)
        new_movies = sorted(new_movies, key=lambda x: -x.vote_avg)
        serializer = MovieListSerializer(new_movies, many=True)
        return Response(serializer.data)
