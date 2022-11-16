import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

const API_URL = "http://127.0.0.1:8000";

export default new Vuex.Store({
  state: {
    movies: [],
    moviesPopular: [],
    moviesNew: [],
  },
  getters: {},
  mutations: {
    GET_POPULAR_MOVIES(state, movies) {
      state.moviesPopular = movies;
    },
    GET_TOP_VOTED_MOVIES(state, movies) {
      state.movies = movies;
    },
    GET_NEW_MOVIES(state, movies) {
      state.moviesNew = movies;
    },
  },
  actions: {
    getPopularMovies(context) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies_popular/`,
      })
        .then((res) => {
          context.commit("GET_POPULAR_MOVIES", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getTopVotedMovies(context) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/`,
      })
        .then((res) => {
          context.commit("GET_TOP_VOTED_MOVIES", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getNewMovies(context) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies_new/`,
      })
        .then((res) => {
          context.commit("GET_NEW_MOVIES", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  modules: {},
});
