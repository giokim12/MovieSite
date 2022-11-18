import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

const API_URL = "http://127.0.0.1:8000";

export default new Vuex.Store({
  state: {
    // JWT START
    access: "",
    refresh: "",
    // JWT END

    // main start
    moviesVoted: [],
    moviesPopular: [],
    moviesOld: [],
    // main end

    // detail start

    // comments: []
  },
  getters: {},
  mutations: {
    // JWT START
    INITAILIZE_STORE(state) {
      if (localStorage.getItem("access")) {
        state.access = localStorage.getItem("access");
        state.refresh = localStorage.getItem("refresh");
      } else {
        state.access = "";
        state.refresh = "";
      }
    },
    SET_ACCESS(state, access) {
      state.access = access;
    },
    SET_REFRESH(state, refresh) {
      state.refresh = refresh;
    },
    REMOVE_ACCESS(state) {
      state.access = "";
      state.refresh = "";
      // state.userdata = "";
      // state.isAuthenticated = false;
    },
    // JWT END

    // main start
    GET_POPULAR_MOVIES(state, movies) {
      state.moviesPopular = movies;
    },
    GET_TOP_VOTED_MOVIES(state, movies) {
      state.moviesVoted = movies;
    },
    GET_OLD_MOVIES(state, movies) {
      state.moviesOld = movies;
    },
    // main end

    // detail start
    //detail end
  },
  actions: {
    //main start
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
    // main end

    // detail start
  },
  modules: {},
});
