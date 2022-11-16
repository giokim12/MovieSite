<template>
  <div id="app">
    <NavBarVue/>
    <!-- <nav>
      <router-link to="/main">Main</router-link> |
      <router-link to="/random">Random</router-link> |
      <router-link to="/watch">Watch</router-link> |
      <router-link to="/signup">signup</router-link> |
      <router-link to="/login">login</router-link> |
    </nav> -->
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
    setInterval(() => {
      this.getAccess()
    }, 59000)
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
    }
  }
    
}
</script>

<style src="./assets/tailwind.css">
/* style src="./assets/tailwind.css" */

/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
} */
</style>
