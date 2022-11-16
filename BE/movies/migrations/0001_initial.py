# Generated by Django 3.2 on 2022-11-16 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
                ('genres', models.ManyToManyField(related_name='movies', to='movies.Genre')),
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
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
    ]
