<template>
  <div id="app">
    <NavBarVue/>
    <router-view />
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
import NavBarVue from "./components/NavBar.vue";


export default {
  name: 'App',
  components: {
    NavBarVue,
  },
  beforeCreate() {
    this.$store.commit('INITAILIZE_STORE')

    const access = this.$store.state.access
    if ( access ) {
      console.log('access')
      axios.defaults.headers.common['Authorization'] = "Bearer " + access
      const accessData = {
        refresh: this.$store.state.refresh
      }

      axios
        .post(`${API_URL}/api/v1/auth/jwt/refresh/`, accessData)
        .then(res => {
          const access = res.data.access
          localStorage.setItem('acccess', access)
          this.$store.commit('SET_ACCESS', access)
        })
        .catch(err => {
          console.log(err)
        })
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/auth/users/me/`,
          headers: {
            Authorization: `Bearer ${this.$store.state.access}`
          }
        })
        .then((res) => {
          this.$store.commit('GET_ME', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    } else {
      console.log('notaccess')
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
  created() {
    setTimeout(() => {
      this.loading = false
    }, 3000)
  },
  computed: {
    isLogin() {
      return this.$store.state.access
    }
  },
  methods: {
    getAccess() {
      const accessData = {
        refresh: this.$store.state.refresh
      }

      axios
        .post(`${API_URL}/api/v1/auth/jwt/refresh/`, accessData)
        .then(res => {
          const access = res.data.access
          localStorage.setItem('acccess', access)
          this.$store.commit('SET_ACCESS', access)
        })
        .catch(err => {
          console.log(err)
        })
    },
    getMe() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/auth/users/me/`,
          headers: {
            Authorization: `Bearer ${this.$store.state.access}`
          }
        })
        .then((res) => {
          this.$store.commit('GET_ME', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
}
window.onbeforeunload = function (e) {

  localStorage.setItem('acccess', '')
  localStorage.setItem('refresh', '');
  localStorage.setItem('vuex', '');


// For IE<8 and Firefox prior to version 4

if (e) {

  localStorage.setItem('acccess', '')
  localStorage.setItem('refresh', '');
  localStorage.setItem('vuex', '');

}



// For Chrome, Safari, IE8+ and Opera 12+

return '페이지를 닫습니다.';

};
</script>

<style src="./assets/tailwind.css"></style>

<style>
#app {
  background-color: black;
}
</style>