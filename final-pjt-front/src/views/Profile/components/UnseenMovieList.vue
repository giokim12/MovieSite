<template>
  <div class="bg-black">
    <h3 class="m-3 flex">
      <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-camera-video-off" viewBox="0 0 16 16">
        <path fill-rule="evenodd" d="M10.961 12.365a1.99 1.99 0 0 0 .522-1.103l3.11 1.382A1 1 0 0 0 16 11.731V4.269a1 1 0 0 0-1.406-.913l-3.111 1.382A2 2 0 0 0 9.5 3H4.272l.714 1H9.5a1 1 0 0 1 1 1v6a1 1 0 0 1-.144.518l.605.847zM1.428 4.18A.999.999 0 0 0 1 5v6a1 1 0 0 0 1 1h5.014l.714 1H2a2 2 0 0 1-2-2V5c0-.675.334-1.272.847-1.634l.58.814zM15 11.73l-3.5-1.555v-4.35L15 4.269v7.462zm-4.407 3.56-10-14 .814-.58 10 14-.814.58z"/>
      </svg>
      <span>
        &nbsp;&nbsp;관심 없는 영화 리스트
      </span>
    </h3>
    <div class="grid grid-cols-6 gap-4">
        <UnseenMovieItem
          v-for="movie in movies_unseen"
          :key="movie.id"
          :movie="movie"
          @unseen="getUnseenMovies()"
        />
    </div>
    <hr>
  </div>
</template>

<script>
import UnseenMovieItem from '@/views/Profile/components/UnseenMovieItem'
// import { Carousel, Slide } from 'vue-carousel';

export default {
  name:'UnseenMovieList',
  components: {
    UnseenMovieItem,
    // Carousel,
    // Slide
  },
  // props: {
  //   movies_unseen: Object
  // }
  // created() {
  //   this.getUnseenMovies()
  // },
  computed: {
    movies_unseen() {
      return this.$store.state.moviesUnseen
    },
  },
  methods: {
    getUnseenMovies() {
      this.$store.dispatch("getUnseenMovies", this.$store.state.userdata.id);
    },
  }
};
</script>

<style>
</style>