from django.urls import path
from . import views

urlpatterns = [
    path('movies/voted/', views.movie_list_voted),
    path('movies/old/', views.movie_list_old),
    path('movies/popular/', views.movie_list_popular),

    path('movies/<int:movie_id>/', views.movie_detail),
    path('movies/actors/<int:movie_id>', views.actor_list),

    path('comments/<int:movie_id>/list/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('movies/<int:movie_id>/comments/', views.comment_create),
]
