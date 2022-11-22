<template>
  <div>
    <div>
      {{ isLogin }}
    </div>
    <MovieList/>
  </div>
</template>

<script>
import MovieList from "@/views/Main/components/MovieList";
export default {
  name: "MainView",
  data() {
    return{
      login: this.$store.state.access
    }
  },
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
      if (this.login) {
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
    },
  },
};

</script>
