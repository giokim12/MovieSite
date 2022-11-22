# Generated by Django 4.1.3 on 2022-11-22 04:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('person_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.IntegerField()),
                ('popularity', models.IntegerField()),
                ('profile_path', models.TextField(null=True)),
                ('biography', models.TextField(null=True)),
                ('birthday', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('rate', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genre_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('popularity', models.IntegerField()),
                ('vote_avg', models.IntegerField()),
                ('overview', models.TextField()),
                ('released_date', models.DateField()),
                ('poster_path', models.TextField(null=True)),
                ('backdrop_path', models.TextField(null=True)),
                ('genres', models.ManyToManyField(related_name='genre_contained_movies', to='movies.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('video_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('key', models.TextField(null=True)),
                ('name', models.CharField(max_length=255)),
                ('iso_639_1', models.CharField(max_length=255)),
                ('published_at', models.CharField(max_length=255)),
                ('iso_3166_1', models.CharField(max_length=255)),
                ('site', models.CharField(max_length=255)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
        migrations.CreateModel(
            name='UnseenMovies',
            fields=[
                ('unseen_movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('person_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('popularity', models.IntegerField()),
                ('character', models.CharField(max_length=100)),
                ('profile_path', models.TextField(null=True)),
                ('credit_movies', models.ManyToManyField(related_name='movie_contained_credits', to='movies.movie')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('like_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.comment')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ClickedMovies',
            fields=[
                ('clicked_movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
