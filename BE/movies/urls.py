from django.urls import path
from . import views

urlpatterns = [
    path('movies/voted/', views.movie_list_voted),
    path('movies/old/', views.movie_list_old),
    path('movies/popular/', views.movie_list_popular),
    path('actors/', views.actor_list)
]
