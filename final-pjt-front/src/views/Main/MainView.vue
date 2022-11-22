<template>
  <div>
    <LoadingEvent
      v-if="!isLoading"
    />
    <MovieList
      v-else
    />
  </div>
</template>

<script>
import MovieList from "@/views/Main/components/MovieList";
import LoadingEvent from "@/components/LoadingEvent.vue"
export default {
  name: "MainView",
  data() {
    return{
      login: this.$store.state.access,
      isLoading: false,
    }
  },
  components: {
    MovieList,
    LoadingEvent
  },
  computed: {
    isLogin() {
      return this.$store.state.access
    }
  },
  created() {
    setTimeout(() => {
      this.isLoading = true
    }, 500);
    this.getPopularMovies();
    this.getTopVotedMovies();
    this.getOldMovies();
    if (this.isLogin) {
      this.getClickedMovies();
      this.getAlgoGenre();
      this.getAlgoEuc();
      this.getAlgoPopular();
      this.getAlgoOld();
      this.getAlgoVoted();
    }
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
      this.$store.dispatch("getClickedMovies", this.$store.state.userdata.id);
    },
    getAlgoGenre() {
      this.$store.dispatch("getAlgoGenre", this.$store.state.userdata.id);
    },
    getAlgoEuc() {
      this.$store.dispatch("getAlgoEuc", this.$store.state.userdata.id);
    },
    getAlgoPopular() {
      this.$store.dispatch("getAlgoPopular", this.$store.state.userdata.id);
    },
    getAlgoOld() {
      this.$store.dispatch("getAlgoOld", this.$store.state.userdata.id);
    },
    getAlgoVoted() {
      this.$store.dispatch("getAlgoVoted", this.$store.state.userdata.id);
    },
  },
};
</script>
