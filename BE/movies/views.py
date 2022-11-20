from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie, Genre, Credit, Comment, ClickedMovies, Video
from .serializers import MovieListSerializer, ActorSerializer, MovieSerializer, CommentSerializer, ClickedMovieSerializer, VideoSerializer
import random

# Create your views here.


@api_view(['GET'])
def movie_list_voted(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        voted_movies = []
        for movie in movies:
            if movie.vote_avg > 5:
                voted_movies.append(movie)
        # print(len(voted_movies)) 
        # print(new_movies[0].vote_avg)
        voted_movies = sorted(voted_movies, key=lambda x: -x.vote_avg)
        voted_movies30 = voted_movies[:30]
        voted_movies6 = random.sample(voted_movies30, 6)
        serializer = MovieListSerializer(voted_movies6, many=True)
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
        old_movies30 = old_movies[:30]
        old_movies6 = random.sample(old_movies30, 6)
        serializer = MovieListSerializer(old_movies6, many=True)
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
        popular_movies30 = popular_movies[:30]
        popular_movies6 = random.sample(popular_movies30, 6)
        serializer = MovieListSerializer(popular_movies6, many=True)
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
        user_clicked_movies = sorted(
            clicked_movies, key=lambda x: -x.clicked_movie_id)
        # print(user_clicked_movies)
        movies = get_list_or_404(Movie)
        show_movies = []

        for clicked_movie in user_clicked_movies:
            for movie in movies:
                if clicked_movie.movie_id == movie.movie_id:
                    show_movies.append(movie)

        result = []
        for show_movie in show_movies:
            if show_movie not in result:
                result.append(show_movie)
        result6 = result[:6]

        serializer = MovieListSerializer(result6, many=True)
        return Response(serializer.data)
'''
# 내가 클릭한 영화들과 같은 장르 가진 영화들 모두 추출
@api_view(['GET'])
def movie_list_genre_recommend(request, user_id):
    clicked_movies = get_list_or_404(ClickedMovies)
    movies = get_list_or_404(Movie)

    # 해당 사용자가 클릭한 영화만 뽑아서 user_clicked_movies 에 넣기
    user_clicked_movies = []
    for clicked_movie in clicked_movies:
        if user_id == clicked_movie.user_id:
            user_clicked_movies.append(clicked_movie) 

    # 클릭한 영화의 정보를 가져와서 clicked_movies_info에 넣기
    clicked_movies_info = []
    for clicked_movie in user_clicked_movies:
        for movie in movies:
            if clicked_movie.movie_id == movie.movie_id:
                clicked_movies_info.append(movie)
    # print(clicked_movies_info)
    # 중복제거
    clicked_movies_info_unique = []
    for clicked_movie_info in clicked_movies_info:
        if clicked_movie_info not in clicked_movies_info_unique:
            clicked_movies_info_unique.append(clicked_movie_info)
    print(clicked_movies_info_unique)

    # 사용자가 클릭한 영화의 장르 중복없이 뽑기
    genres = []
    for clicked_movie in clicked_movies_info_unique:
        a = clicked_movie.genres.all()
        for b in a:
            genres.append(b.name)

    genre_unique = []
    for g in genres:
        if g not in genre_unique:
            genre_unique.append(g)
    # print(genre_unique)

    movies_recommend =[]
    for movie in movies:
        mg = movie.genres.all()
        for i in genre_unique:
            # print(i)
            for g in mg:
                # print(g.name)
                if g.name == i:
                    movies_recommend.append(movie)
    # print(movies_recommend)
    # 중복제거 후 출력
    result = []
    for movie_recommend in movies_recommend:
        if movie_recommend not in result:
            result.append(movie_recommend)
    # print("-------------------------")
    # print(result)
    # print("---------------------------")
    result6 = result[:6]
    serializer = MovieListSerializer(result6, many=True)
    return Response(serializer.data)
'''

@api_view(['GET'])
def movie_list_genre_recommend(request, user_id):
    clicked_movies = get_list_or_404(ClickedMovies)
    movies = get_list_or_404(Movie)

    # 해당 사용자가 클릭한 영화만 뽑아서 user_clicked_movies 에 넣기
    user_clicked_movies = []
    for clicked_movie in clicked_movies:
        if user_id == clicked_movie.user_id:
            user_clicked_movies.append(clicked_movie)

    # 클릭한 영화의 정보를 가져와서 clicked_movies_info에 넣기
    clicked_movies_info = []
    for clicked_movie in user_clicked_movies:
        for movie in movies:
            if clicked_movie.movie_id == movie.movie_id:
                clicked_movies_info.append(movie)
    # bucket1 = [1]*len(clicked_movies_info)
    # 중복제거
    user_clicked_movies_unique = []
    for clicked_movie_info in clicked_movies_info:
        if clicked_movie_info not in user_clicked_movies_unique:
            user_clicked_movies_unique.append(clicked_movie_info)
    
    bucket = [0]*len(user_clicked_movies_unique)
    # 해당 사용자가 클릭 더 많이 할수록 가중치
    for i in range(len(user_clicked_movies_unique)):
        for j in range(len(clicked_movies_info)):
            if user_clicked_movies_unique[i] == clicked_movies_info[j]:
                bucket[i] +=1

    movies_bucket = [0]*len(movies)
    for i in range(len(user_clicked_movies_unique)):
        for j in clicked_movies_info[i].genres.all():
            for k in range(len(movies)):
                for l in movies[k].genres.all():
                    if j == l:
                        movies_bucket[k] += bucket[i]
    
    # print(movies_bucket)

    result = random.choices(movies, movies_bucket, k = 6)
    serializer = MovieListSerializer(result, many=True)
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
        serializer = ClickedMovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movie_detail_video(request, movie_id):

    video = get_list_or_404(Video, movie_id=movie_id)
    print(video)
    get_video = video[:1]
    print(get_video)
    if request.method == 'GET':
        serializer = VideoSerializer(get_video, many=True)
        print(serializer.data)
        return Response(serializer.data)


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
