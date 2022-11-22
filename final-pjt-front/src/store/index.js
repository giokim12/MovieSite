import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

const API_URL = "http://127.0.0.1:8000";

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    // JWT START
    access: "",
    refresh: "",
    userdata: "",
    // JWT END

    // main start
    moviesVoted: [],
    moviesPopular: [],
    moviesOld: [],
    moviesClicked: [],
    moviesAlgoGenre: [],
    moviesAlgoEuc: [],
    moviesAlgoPopular: [],
    moviesAlgoOld: [],
    moviesAlgoVoted: [],

    // main end

    // detail start

    comments: [],
    moviesSimilar: [],
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
      console.log("access = ", access);
      state.access = access;
    },
    SET_REFRESH(state, refresh) {
      state.refresh = refresh;
    },
    GET_ME(state, me) {
      state.userdata = me;
    },
    REMOVE_ACCESS(state) {
      state.access = "";
      state.refresh = "";
      state.userdata = "";
      state.isAuthenticated = false;
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
    GET_CLICKED_MOVIES(state, movies) {
      state.moviesClicked = movies;
    },
    GET_ALGO_GENRES(state, movies) {
      state.moviesAlgoGenre = movies;
    },
    GET_ALGO_EUC(state, movies) {
      state.moviesAlgoEuc = movies;
    },
    GET_ALGO_POPULAR(state, movies) {
      state.moviesAlgoPopular = movies;
    },
    GET_ALGO_OLD(state, movies) {
      state.moviesAlgoOld = movies;
    },
    GET_ALGO_VOTED(state, movies) {
      state.moviesAlgoVoted = movies;
    },
    // main end

    // detail start
    GET_COMMENT_LIST(state, comments) {
      state.comments = [];
      state.comments = comments;
    },
    NOT_COMMENT_LIST(state) {
      state.comments = [];
    },
    GET_SIMILAR_MOVIES(state, movies) {
      state.moviesSimilar = movies;
    },
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
    getClickedMovies(context, user_id) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/clicked/${user_id}/`,
      })
        .then((res) => {
          context.commit("GET_CLICKED_MOVIES", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getAlgoGenre(context, user_id) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/recommend/genre/${user_id}/`,
      })
        .then((res) => {
          context.commit("GET_ALGO_GENRES", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getAlgoEuc(context, user_id) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/recommend/euclidean/${user_id}/`,
      })
        .then((res) => {
          context.commit("GET_ALGO_EUC", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getAlgoPopular(context, user_id) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/popular/${user_id}/`,
      })
        .then((res) => {
          context.commit("GET_ALGO_POPULAR", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getAlgoOld(context, user_id) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/old/${user_id}/`,
      })
        .then((res) => {
          context.commit("GET_ALGO_OLD", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getAlgoVoted(context, user_id) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/voted/${user_id}/`,
      })
        .then((res) => {
          context.commit("GET_ALGO_VOTED", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    // main end

    // detail start
    getCommentList(context, movie_id) {
      // this.$store.dispatch("getCommentList", this.$route.params.movie_id)
      axios({
        method: "get",
        url: `${API_URL}/api/v1/comments/${movie_id}/list/`,
      })
        .then((res) => {
          context.commit("GET_COMMENT_LIST", res.data);
        })
        .catch((err) => {
          console.log(err);
          context.commit("NOT_COMMENT_LIST");
        });
    },
    getSimilarMovies(context, movie_id) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/similar/${movie_id}/`,
      })
        .then((res) => {
          context.commit("GET_SIMILAR_MOVIES", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  modules: {},
});
