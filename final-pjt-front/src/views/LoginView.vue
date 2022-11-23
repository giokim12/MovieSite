<template>
  <div>
    <section class="bg-black h-screen">
      <!-- <img src="../assets/jwt-bg.png" alt="bg">  -->
      <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-full lg:py-0">
        <div class="flex items-center mb-6">
            <img class="w-80 h-60 mr-2 text-white" src="../assets/logo.png" alt="logo">  
        </div>
        <div class="w-full bg-black rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 ">
          <div class="p-6 space-y-4 md:space-y-6 sm:p-8 bg-black opacity-75 rounded-xl border border-white">
              <h1 class="text-xl text-white font-bold leading-tight tracking-tight md:text-2xl">
                  로그인
              </h1>
              <form v-on:submit.prevent="submitForm" class="space-y-4 md:space-y-6" action="#">
                  <div>
                      <label for="username" class="block mb-2 text-sm font-medium text-white">아이디</label>
                      <input v-model="username" type="text" name="username" id="username" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5" required="">
                  </div>
                  <div>
                      <label for="password" class="block mb-2 text-sm font-medium text-white">비밀번호</label>
                      <input v-model="password" type="password" name="password" id="password" placeholder="••••••••" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5" required="">
                  </div>
                  <button type="submit" class="w-full text-white bg-red-400 hover:bg-red-500 focus:ring-4 focus:outline-none focus:ring-red-200 font-medium rounded-lg text-sm px-5 py-2.5 text-center">로그인</button>
                  <p class="text-sm font-light text-white">
                      JWT 회원이 아닌가요?
                      <router-link to="/signup" class="font-medium text-red-300 hover:underline hover:text-red-400">지금 가입하세요.</router-link>
                  </p>
              </form>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name:'LoginView',
  data () {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    submitForm() {
      axios.defaults.headers.common['Authorization'] = ''
      localStorage.removeItem('access')
      const formData = {
        username: this.username,
        password: this.password,
      }
      console.log(formData)

      axios
        .post(`${API_URL}/api/v1/auth/jwt/create/`, formData)
        .then((res) => {
          console.log(res)
          const access = res.data.access
          const refresh = res.data.refresh

          this.$store.commit('SET_ACCESS', access)
          this.$store.commit('SET_REFRESH', refresh)

          axios.defaults.headers.common['Authorization'] = "JWT " + access

          localStorage.setItem('access', access)
          localStorage.setItem('refresh', refresh)

          
          this.$router.push('/')
          this.getMe()
        })
        .catch((err) => {
          console.log(err);
        });
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
};
</script>

<style>
</style>