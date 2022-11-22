<template>
  <div>
    <MovieList/>
  </div>
</template>

<script>
import MovieList from "@/views/Main/components/MovieList";
export default {
  name: "MainView",
  components: {
    MovieList,
  },
  computed: {
    isLogin() {
      return this.$store.state.access
    }
  },
};

</script>
