from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie, Genre, Credit, Comment, ClickedMovies
from .serializers import MovieListSerializer, ActorSerializer, MovieSerializer, CommentSerializer
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
# @permission_classes((IsAuthenticated, ))
def movie_list_clicked(request, user_id):
    if request.method == 'GET':
        clicked_movies = get_list_or_404(ClickedMovies)
        user_clicked_movies = []
        for clicked_movie in clicked_movies:
            if user_id == clicked_movie.user_id:
                user_clicked_movies.append(clicked_movie)
        user_clicked_movies = sorted(clicked_movies, key=lambda x: -x.clicked_movie_id)
        movies = get_list_or_404(Movie)
        show_movies = []

        for clicked_movie in user_clicked_movies:
            for movie in movies:
                if clicked_movie.movie_id == movie.movie_id:
                    show_movies.append(movie)      
        
        show_movies = set(show_movies)
        serializer = MovieListSerializer(show_movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def actor_list(request, movie_id):
    if request.method == 'GET':
        actors = get_list_or_404(Credit, movie=movie_id)
        actors_5 = actors[:5]
        serializer = ActorSerializer(actors_5, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def movie_detail(request, movie_id):
    # article = Article.objects.get(pk=article_pk)
    print(request)
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = ClickedMovieSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)       



@api_view(['GET'])
def comment_list(request, movie_id):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment, movie=movie_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def comment_create(request, movie_id):
    # article = Article.objects.get(pk=article_pk)
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

