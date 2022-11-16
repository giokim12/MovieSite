<template>
  <nav>
    <div :src="user_data">{{ user_data }}</div>
    <router-link to="/main">Main</router-link> |
    <router-link to="/random">Random</router-link> |
    <router-link to="/watch">Watch</router-link> |
    <span v-if="!isLogin"><router-link to="/signup">signup</router-link> |</span>
    <span v-if="!isLogin"><router-link to="/login">login</router-link> |</span>
    <button v-if="isLogin" @click="logout">logout</button>
  </nav>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: 'NavBar',
  data() {
    return {
      user_data: ''
    }
  },
  computed: {
    isLogin() {
      return this.$store.state.access
    }
  },
  mounted() {
    this.getMe()
  },
  methods: {
    getMe() {
      axios
        .get(`${API_URL}/api/v1/auth/users/me/`)
        .then((res) => {
          console.log(res)
          this.user_data = res.data.username
        })
        .catch(err => {
          console.log(err)
        })
    },
    logout() {
      this.$store.commit('REMOVE_ACCESS');
      localStorage.setItem('access', '');
      localStorage.setItem('refresh', '');
    }
  }
}
</script>

<style>

</style>