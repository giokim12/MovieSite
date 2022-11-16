import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  state: {
    movies: [],
  },
  getters: {
  },
  mutations: {
    GET_POPULAR_MOVIES(state, movies) {
      state.movies = movies
    }
  },
  actions: {
    getPopularMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/`,
        // headers: {
        //   Authorization: `Token ${context.state.token}`
        // }
      })
        .then((res) => {
          // console.log(res, context)
          // console.log(res.data)
          context.commit('GET_POPULAR_MOVIES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      }
  },
  modules: {
  }
})
