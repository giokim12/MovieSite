<template>
  <div class="bg-black h-[100vh] text-white">
    {{ movies_unseen }}
  </div>
</template>

<script>
export default {
  name:'UnseenMovieView',
  created() {
    this.getUnseenMovies()
  },
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