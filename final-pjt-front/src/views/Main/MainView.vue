<template>
  <div id="back">
    <h1 class="text-white">이거는 메인 페이지</h1>
    <MovieList />
  </div>
</template>

<script>
import MovieList from "@/views/Main/components/MovieList";

export default {
  name: "MainView",
  components: {
    MovieList,
  },
  created() {
    this.getPopularMovies();
    this.getTopVotedMovies();
    this.getOldMovies();
  },
  methods: {
    getPopularMovies() {
      this.$store.dispatch("getPopularMovies");
    },
    getTopVotedMovies() {
      this.$store.dispatch("getTopVotedMovies");
    },
    getOldMovies() {
      this.$store.dispatch("getOldMovies");
    },
  },
};
</script>

<style>
/* #back{
  background-color: #141414;
} */
</style>
