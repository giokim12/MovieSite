<template>
  <div>
    <h2 class="text-white">투표 내림차순 정렬</h2>
    <div class="flex">
      <MovieListItem
        v-for = "(movie, idx) in movies_voted"
        :key = "`movie${idx}`"
        :movie = "movie"
      />
    </div>
    <hr>
    <h2 class="text-white">인기도 내림차순 정렬</h2>
    <div class="flex">
      <MovieListItem
        v-for = "(movie, idx) in movies_popular"
        :key = "idx"
        :movie = "movie"
        class="flex"
      />
    </div>
    <hr>
    <h2 class="text-white">고전명작,,, 개봉일 오름차순 정렬</h2>
    <div class="flex">
      <MovieListItem
        v-for = "(movie, idx) in movies_old"
        :key = "idx"
        :movie = "movie"
        class="flex"
      />
    </div>
    <hr>
    <h2 class="text-white">클릭한거</h2>
    <div class="flex">
      <MovieListItem
        v-for = "(movie, idx) in movies_clicked"
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
    movies_voted () {
      return this.$store.state.moviesVoted
    },
    movies_popular () {
      return this.$store.state.moviesPopular
    },
    movies_old () {
      return this.$store.state.moviesOld
    },
    movies_clicked () {
      return this.$store.state.moviesClicked
    }
  }
}


</script>

<style>

</style>