from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies_new/', views.movie_list_new),
    path('movies_popular/', views.movie_list_popular),
    path('actors/', views.actor_list)
]
