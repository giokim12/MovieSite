<template>
  <div>
    <div class="grid grid-cols-6 gap-4">
        <UnseenMovieItem
          v-for="movie in movies_unseen"
          :key="movie.id"
          :movie="movie"
        />
    </div>
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
  // methods: {
  //   getUnseenMovies() {
  //     this.$store.dispatch("getUnseenMovies", this.$store.state.userdata.id);
  //   },
  // }
};
</script>

<style>
</style>