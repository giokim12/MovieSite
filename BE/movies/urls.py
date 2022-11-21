from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('movies/voted/', views.movie_list_voted),
    path('movies/old/', views.movie_list_old),
    path('movies/popular/', views.movie_list_popular),

    path('movies/clicked/<int:user_id>/', views.movie_list_clicked),
    path('movies/recommend/genre/<int:user_id>/',
         views.movie_list_genre_recommend),
    path('movies/recommend/euclidean/<int:user_id>/',
         views.movie_list_euclidean_recommend),

    path('detail/<int:movie_id>/', views.movie_detail),
    path('detail/video/<int:movie_id>/', views.movie_detail_video),
    path('movies/actors/<int:movie_id>/', views.actor_list),
    path('movies/similar/<int:movie_id>/', views.movie_list_similar),

    path('comments/<int:movie_id>/list/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('movies/<int:movie_id>/comments/', views.comment_create),

    path('comments/like/detail/<int:comment_id>/', views.comment_like_detail),
    path('comments/like/list/<int:comment_id>/', views.comment_like_list),
    path('comments/like/<int:comment_id>/', views.comment_like_create),

    # # 필수 작성
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # optional UI
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),

]
