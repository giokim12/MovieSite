import requests
import json
import os
TMDB_API_KEY = '94cfb0b050444c186251cd8dee48a17d'

movie_id = []


def get_movie_datas():
    total_data = []
    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for i in range(1, 10):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('adult') == False and movie.get('release_date', ''):
                fields = {
                    'movie_id': movie['id'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_avg': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids']
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }
                movie_id.append(movie['id'])
                total_data.append(data)

    with open("movie.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)


def get_credit_datas():
    total_data = []
    for mid in movie_id:
        request_url = f"https://api.themoviedb.org/3/movie/{mid}/credits?api_key={TMDB_API_KEY}&language=ko-KR"
        get_credits = requests.get(request_url).json()
        for credit in get_credits['cast']:
            if credit.get('popularity') > 5 and credit.get('profile_path') != '':
                fields = {
                    'person_id': credit['id'],
                    "movie_id": mid,
                    'name': credit['name'],
                    'popularity': credit['popularity'],
                    'character': credit['character'],
                    'profile_path': credit['profile_path'],
                }
                data = {
                    'model': "movies.credit",
                    "fields": fields
                }
                total_data.append(data)
    print(len(total_data))
    with open("credit.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)


get_movie_datas()
get_credit_datas()
