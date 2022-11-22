from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie, Genre, Credit, Comment, ClickedMovies, Video, CommentLike, UnseenMovies
from .serializers import MovieListSerializer, ActorSerializer, MovieSerializer, CommentSerializer, ClickedMovieSerializer, VideoSerializer, CommentLikeSerializer, UnseenMovieSerializer
import random

# Create your views here.
# 001 movie_list
# 002 movie_detail
# 003 movie_unseen
# 004
# 005

# 001


@api_view(['GET'])
def movie_list_voted(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        voted_movies = []
        for movie in movies:
            if movie.vote_avg > 5:
                voted_movies.append(movie)
        voted_movies = sorted(voted_movies, key=lambda x: -x.vote_avg)
        voted_movies150 = voted_movies[:150]
        voted_movies30 = random.sample(voted_movies150, 30)
        serializer = MovieListSerializer(voted_movies30, many=True)
        return Response(serializer.data)

# 001


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

# 001


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

# 001


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

# 001


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
                bucket[i] += 1

    movies_bucket = [0]*len(movies)
    for i in range(len(user_clicked_movies_unique)):
        for j in clicked_movies_info[i].genres.all():
            for k in range(len(movies)):
                for l in movies[k].genres.all():
                    if j == l:
                        movies_bucket[k] += bucket[i]
    # print(movies_bucket)

    result = random.choices(movies, movies_bucket, k=6)
    serializer = MovieListSerializer(result, many=True)
    return Response(serializer.data)

# 001
# 유사도측정(유클리디안 거리)


@api_view(['GET'])
def movie_list_euclidean_recommend(request, user_id):
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

    # 클릭한 영화 중복제거
    # # bucket1 = [1]*len(clicked_movies_info)
    user_clicked_movies_unique = []
    for clicked_movie_info in clicked_movies_info:
        if clicked_movie_info not in user_clicked_movies_unique:
            user_clicked_movies_unique.append(clicked_movie_info)

    # 클릭한 영화의 인기도랑 투표수만 가져와서 배열에 넣기
    user_clicked_movies_numbers = []
    for user_clicked_movie_unique in user_clicked_movies_unique:
        user_clicked_movies_numbers.append(
            [user_clicked_movie_unique.vote_avg, user_clicked_movie_unique.popularity])
    # print(user_clicked_movies_numbers)

    # 모든 영화의 인기도랑 투표수만 가져와서 배열에 넣기
    movies_numbers = []
    for movie in movies:
        movies_numbers.append([movie.vote_avg, movie.popularity])
    # print(movies_numbers)

    # 유클리디안 거리 구하기
    euc = []
    for user_clicked_movie_numbers in user_clicked_movies_numbers:
        for i in range(len(movies_numbers)):
            temp = []
            dist = ((movies_numbers[i][0]-user_clicked_movie_numbers[0])**2 + (
                movies_numbers[i][1]-user_clicked_movie_numbers[1])**2)**(1/2)
            if dist != 0:
                temp.append(dist)
                temp.append(movies[i])
                euc.append(temp)

    euc = sorted(euc, key=lambda x: x[0])
    # 중복 없애기
    result = []
    for e in euc:
        if e not in result:
            result.append(e)

    final_result = []
    for k in result:
        final_result.append(k[1])

    result6 = final_result[:6]

    serializer = MovieListSerializer(result6, many=True)
    return Response(serializer.data)

# 002


@api_view(['GET'])
def actor_list(request, movie_id):
    if request.method == 'GET':
        actors = get_list_or_404(Credit, movie=movie_id)
        actors_5 = actors[:10]
        serializer = ActorSerializer(actors_5, many=True)
        return Response(serializer.data)

# 002


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

# 002


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

# 내가 디테일 페이지 들어간 영화랑 같은 장르 가진 영화들 모두 추출

# 002


@api_view(['GET'])
def movie_list_similar(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    movies = get_list_or_404(Movie)

    # 이 영화의 장르 중복없이 뽑기
    genres = []
    a = movie.genres.all()
    for b in a:
        genres.append(b.name)

    movies_recommend = []
    for genre in genres:
        for m in movies:
            g = m.genres.all()
            for i in g:
                if i.name == genre:
                    movies_recommend.append(m)

    # # 중복제거 후 출력
    result = []
    for movie_recommend in movies_recommend:
        if movie_recommend not in result:
            result.append(movie_recommend)

    result6 = result[:6]
    serializer = MovieListSerializer(result6, many=True)
    return Response(serializer.data)

# 002


@api_view(['GET'])
def comment_list(request, movie_id):
    if request.method == 'GET':
        comments = get_list_or_404(Comment, movie=movie_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

# 002


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
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

# 002


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def comment_create(request, movie_id):
    # article = Article.objects.get(pk=article_pk)
    movie = get_object_or_404(Movie, pk=movie_id)
    print(request.data)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 002


@api_view(['GET'])
def comment_like_list(request, comment_id):
    if request.method == 'GET':
        comment_likes = get_list_or_404(CommentLike, comment_id=comment_id)
        serializer = CommentLikeSerializer(comment_likes, many=True)
        return Response(serializer.data)

# 002


@api_view(['DELETE'])
@permission_classes((IsAuthenticated, ))
def comment_like_detail(request, comment_id):
    likes = get_list_or_404(CommentLike, comment_id=comment_id)

    # print(request.data['user_id'])
    if request.method == 'DELETE':
        for like in likes:
            if str(like.user_id) == str(request.data['user_id']):
                # print('qwdqwdqdqwdqwdqqwd')
                # serializer = CommentLikeSerializer(data=request.data)
                # print(serializer.data)
                data = {
                    'message': 'del'
                }
                like.delete()
                return Response(data, status=status.HTTP_204_NO_CONTENT)
            else:
                print('qwdwq')

# 002


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def comment_like_create(request, comment_id):

    comment = get_object_or_404(Comment, comment_id=comment_id)
    if request.method == 'POST':
        serializer = CommentLikeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(comment_id=comment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


def user_profile():
    pass

# 003


@api_view(['POST'])
def movie_unseen(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == "POST":
        serializer = UnseenMovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 003


@api_view(['GET'])
def movie_list_unseen(request, user_id):
    if request.method == 'GET':
        unseen_movies = get_list_or_404(UnseenMovies)
        user_unseen_movies = []
        for unseen_movie in unseen_movies:
            if user_id == unseen_movie.user_id:
                user_unseen_movies.append(unseen_movie)
        movies = get_list_or_404(Movie)
        show_movies = []

        for unseen_movie in user_unseen_movies:
            for movie in movies:
                if unseen_movie.movie_id == movie.movie_id:
                    show_movies.append(movie)

        result = []
        for show_movie in show_movies:
            if show_movie not in result:
                result.append(show_movie)

        serializer = MovieListSerializer(result, many=True)
        return Response(serializer.data)
