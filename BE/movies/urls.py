from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('movies/voted/', views.movie_list_voted),
    path('movies/old/', views.movie_list_old),
    path('movies/popular/', views.movie_list_popular),

    path('movies/<int:movie_id>/', views.movie_detail),
    path('movies/actors/<int:movie_id>', views.actor_list),

    path('comments/<int:movie_id>/list/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('movies/<int:movie_id>/comments/', views.comment_create),

    # # 필수 작성
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # optional UI
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
]
