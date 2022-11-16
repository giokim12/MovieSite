from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('actors/', views.actor_list)
]
