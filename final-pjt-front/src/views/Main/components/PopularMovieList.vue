<template>
  <div>
    <h2>유명도(?)에 따른 내림차순 정렬입니당</h2>
    <MovieListItem
      v-for = "movie in movies"
      :key = "movie.id"
      :movie = "movie"
    />
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
    }
  }

}
</script>

<style>

</style>