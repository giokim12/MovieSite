<template>
  <div class="flex">
    <hr>
    <div class="flex grid grid-cols-6 gap-4">
      <MovieListItem
        v-for = "(movie, idx) in movies_similar"
        :key = "idx"
        :movie = "movie"
      />
    </div>
  </div>

</template>

<script>
import MovieListItem from '@/views/Main/components/MovieListItem'
export default {
  name: "SimilarMovieList",
  components: {
    MovieListItem,
  },
  computed: {
    movies_similar() {
      return this.$store.state.moviesSimilar
    }
  }
}
</script>

<style>

</style>