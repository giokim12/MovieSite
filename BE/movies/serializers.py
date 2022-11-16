from rest_framework import serializers
from .models import Movie, Genre, Credit

# 영화 리스트


class MovieListSerializer(serializers.ModelSerializer):
    class GenreNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)
    genres = GenreNameSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('title', 'overview', 'genres', 'vote_avg')


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        fields = ('person_id', 'name', 'popularity',
                  'character', 'profile_path')
