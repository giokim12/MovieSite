<template>
  <div class="bg-black h-[1000px]">
    <h3 class="text-white ml-5 mt-4">{{this.$route.params.search}} 검색 결과</h3>
    <div class="flex flex-wrap mx-auto bg-black">
      <MovieListItemVue
        v-for="movie in search_movies"
        :key="movie.id"
        :movie="movie"
        class="inline-block w-[33%] lg:w-[25%] pl-3"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import MovieListItemVue from "./Main/components/MovieListItem.vue";
const API_URL = "http://127.0.0.1:8000";
export default {
  name:'SearchView',
  data() {
    return{
      movies: null,
      isSearch: this.$route.params.search
    }
  },
  components: {
    MovieListItemVue
  },
  computed: {
    search_movies() {
      return this.movies
    },
    is_search() {
      return this.$store.state.isSearch
    }
  },
  created() {
    this.getSearchMovies()
  },
  methods: {
    getSearchMovies() {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/search/${this.$route.params.search}/`,
      })
        .then((res) => {
          this.movies = res.data
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  watch: {
    is_search: function() {
      this.getSearchMovies()
    }
  }
}
</script>

<style>

</style>