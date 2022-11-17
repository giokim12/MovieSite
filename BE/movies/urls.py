from django.urls import path
from . import views

urlpatterns = [
    path('movies/voted/', views.movie_list_voted),
    path('movies/old/', views.movie_list_old),
    path('movies/popular/', views.movie_list_popular),
    path('movies/actors/', views.actor_list),
    # path('movies/<int:movie_pk>/', views.movie_detail)
]
