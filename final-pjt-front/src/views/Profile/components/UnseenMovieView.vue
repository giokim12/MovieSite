<template>
  <div class="bg-black h-[100vh] text-white">
    <UnseenMovieList/>
  </div>
</template>

<script>
import UnseenMovieList from '@/views/Profile/components/UnseenMovieList'
export default {
  name:'UnseenMovieView',
  data() {
    return{
      login: this.$store.state.access
    }
  },
  components: {
    UnseenMovieList,
  },
  computed: {
    isLogin() {
      return this.$store.state.access
    }
  },
  created() {
    this.getUnseenMovies()
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