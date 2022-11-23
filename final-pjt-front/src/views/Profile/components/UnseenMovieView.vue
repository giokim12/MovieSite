<template>
  <!-- <div class="h-screen"> -->
    <div class="bg-black text-white h-screen">
        <UnseenMovieList
        />
    </div>
  <!-- </div> -->
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
    this.isLoginCheck()
  },
  methods: {
    isLoginCheck() {
      if (!this.$store.state.userdata) {
        this.$router.push({ name: 'login'})
      }
    },
    getUnseenMovies() {
      this.$store.dispatch("getUnseenMovies", this.$store.state.userdata.id);
    },
  }
};
</script>

<style>
</style>