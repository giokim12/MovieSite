<template>
  <div>
    <h1>이거는 메인 페이지</h1>
    <PopularMovieList/>
  </div>
</template>

<script>
import PopularMovieList from '@/views/Main/components/PopularMovieList'

export default {
  name: 'MainView',
  components: {
    PopularMovieList,
  },
  created() {
    this.getPopularMovies()
    this.getTopVotedMovies()
    this.getNewMovies()
  },
  methods: {
    getPopularMovies() {
      this.$store.dispatch('getPopularMovies')
    },
    getTopVotedMovies() {
      this.$store.dispatch('getTopVotedMovies')
    },
    getNewMovies() {
      this.$store.dispatch('getNewMovies')
    },
  }
};
</script>

<style>
</style>