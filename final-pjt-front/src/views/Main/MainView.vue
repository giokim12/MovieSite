<template>
  <div>
    <h1>이거는 메인 페이지</h1>
    <MovieList/>
  </div>
</template>

<script>


export default {
  name: 'MainView',
  components: {
    MovieList,
  },
  created() {
    this.getPopularMovies()
    this.getTopVotedMovies()
    this.getOldMovies()
  },
  methods: {
    getPopularMovies() {
      this.$store.dispatch('getPopularMovies')
    },
    getTopVotedMovies() {
      this.$store.dispatch('getTopVotedMovies')
    },
    getOldMovies() {
      this.$store.dispatch('getOldMovies')
    },
  }
};
</script>

<style>
</style>