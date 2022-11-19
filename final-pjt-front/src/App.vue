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
      axios.defaults.headers.common['Authorization'] = "JWT " + access
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
  mounted(){
    const access = this.$store.state.access
    if (access !== '') {
      setInterval(() => {
        this.getAccess()
        this.getMe()
      }, 59000)
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
  }
    
}
</script>

<style src="./assets/tailwind.css"></style>

<style>
#app {
  background-color: #141414;
}
</style>