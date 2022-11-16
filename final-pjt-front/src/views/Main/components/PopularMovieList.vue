<template>
  <div>
    <h2>유명도(?)에 따른 내림차순 정렬입니당</h2>
    <div class="flex">
      <MovieListItem
        v-for = "(movie, idx) in movies"
        :key = "`movie${idx}`"
        :movie = "movie"
      />
    </div>
    <hr>
    <h2>popular</h2>
    <div class="flex">
      <MovieListItem
        v-for = "(movie, idx) in movies_popular"
        :key = "idx"
        :movie = "movie"
        class="flex"
      />
    </div>
    <hr>
    <h2>new</h2>
    <div class="flex">
      <MovieListItem
        v-for = "(movie, idx) in movies_new"
        :key = "idx"
        :movie = "movie"
        class="flex"
      />
    </div>
  </div>
</template>

<script>
import MovieListItem from '@/views/Main/components/MovieListItem'

export default {
  name: "PopularMovieList",
  components: {
    MovieListItem
  },
  computed: {
    movies () {
      return this.$store.state.movies
    },
    movies_popular () {
      return this.$store.state.moviesPopular
    },
    movies_new () {
      return this.$store.state.moviesNew
    }
  }
}


</script>

<style>

</style>