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
  },
  methods: {
    getPopularMovies() {
      this.$store.dispatch('getPopularMovies')
    },
  }
};
</script>

<style>
</style>