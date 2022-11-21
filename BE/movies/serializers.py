from rest_framework import serializers
from .models import Movie, Genre, Credit, Comment, ClickedMovies, Video, CommentLike

# 영화 리스트


class MovieListSerializer(serializers.ModelSerializer):
    class GenreNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)
    genres = GenreNameSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('movie_id', 'title', 'overview', 'genres',
                  'vote_avg', 'released_date', 'popularity', 'poster_path', 'backdrop_path')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie',)


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class GenreNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)
    genres = GenreNameSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class ClickedMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClickedMovies
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = '__all__'
