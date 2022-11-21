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
  computed: {
    isLogin() {
      return this.$store.state.access
    }
  },
  created() {
    this.getPopularMovies();
    this.getTopVotedMovies();
    this.getOldMovies();
    this.getClickedMovies();
    this.getAlgoGenre();
    this.getAlgoEuc();
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
    getClickedMovies() {
      if (this.isLogin) {
        this.$store.dispatch("getClickedMovies", this.$store.state.userdata.id);
      }
    },
    getAlgoGenre() {
      if (this.isLogin) {
        this.$store.dispatch("getAlgoGenre", this.$store.state.userdata.id);
      }
    },
    getAlgoEuc() {
      if (this.isLogin) {
        this.$store.dispatch("getAlgoEuc", this.$store.state.userdata.id);
      }
    }
  },
};
</script>

<style>
/* #back{
  background-color: #141414;
} */
</style>
