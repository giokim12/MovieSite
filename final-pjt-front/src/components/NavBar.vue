<template>
    <nav class="px-1 sm:px-4 rounded">
      <div class="container flex flex-wrap items-center justify-between mx-auto border-b-2 border-white">
        <div>
          <router-link to="/main">
            <img class="w-15 h-10 mr-2 text-white my-2" src="../assets/small-logo.png" alt="">
          </router-link>
        </div>
        <div>
          <router-link v-if="!isLogin" to="/signup" class="text-white mr-3">회원가입</router-link>
          <router-link v-if="!isLogin" to="/login" class="text-white rounded">로그인</router-link>
          <button v-if="isLogin" class="text-white mr-3">{{ user_data }} 님 환영합니다!</button>
          <button v-if="isLogin" @click="logout" class="text-white">로그아웃</button>
        </div>
      </div>
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