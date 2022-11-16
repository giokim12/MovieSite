import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

const API_URL = "http://127.0.0.1:8000";

export default new Vuex.Store({
  state: {
    moviesVoted: [],
    moviesPopular: [],
    moviesOld: [],
    // comments: []
  },
  getters: {},
  mutations: {
    GET_POPULAR_MOVIES(state, movies) {
      state.moviesPopular = movies;
    },
    GET_TOP_VOTED_MOVIES(state, movies) {
      state.moviesVoted = movies;
    },
    GET_OLD_MOVIES(state, movies) {
      state.moviesOld = movies;
    },
  },
  actions: {
    getPopularMovies(context) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/popular/`,
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
        url: `${API_URL}/api/v1/movies/voted/`,
      })
        .then((res) => {
          context.commit("GET_TOP_VOTED_MOVIES", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getOldMovies(context) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/old/`,
      })
        .then((res) => {
          context.commit("GET_OLD_MOVIES", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  modules: {},
});
