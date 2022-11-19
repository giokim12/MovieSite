from rest_framework import serializers
from .models import Movie, Genre, Credit, Comment

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
                  'vote_avg', 'released_date', 'popularity', 'poster_path')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie',)


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        fields = '__all__'


class MovieSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
