<template>
  <div>
    <section class="bg-black h-screen">
      <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-full lg:py-0">
        <div class="flex items-center mt-8 mb-4">
            <img class="w-80 h-60 mr-2 text-white" src="../assets/logo.png" alt="logo">  
        </div>
        <div class="w-full bg-black rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-2">
          <div class="p-6 space-y-4 md:space-y-6 sm:p-8 bg-black opacity-75 rounded-xl border border-white">
              <h1 class="text-xl font-bold leading-tight tracking-tight text-white md:text-2xl">
                JWT 시작하기
              </h1>
              <form class="space-y-4 md:space-y-6" v-on:submit.prevent="submitForm">
                  <div>
                      <label for="username" class="block mb-2 text-sm font-medium text-white">아이디</label>
                      <input v-model="username" type="text" name="username" id="username" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5" required="">
                  </div>
                  <div>
                      <label for="nickname" class="block mb-2 text-sm font-medium text-white">닉네임</label>
                      <input v-model="nickname" type="text" name="nickname" id="nickname" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5" required="">
                  </div>
                  <div>
                      <label for="password" class="block mb-2 text-sm font-medium text-white">비밀번호</label>
                      <input v-model="password" type="password" name="password" id="password" placeholder="••••••••" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5" required="">
                  </div>
                  <button type="submit" class="w-full text-white bg-red-400 hover:bg-red-500 focus:ring-4 focus:outline-none focus:ring-red-200 font-medium rounded-lg text-sm px-5 py-2.5 text-center">가입하기</button>
                  <p class="text-sm font-light text-white">
                    계정이 있으신가요?
                    <router-link to="/login" class="text-red-300 font-medium hover:text-red-400">로그인</router-link>
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
  name:'SignupView',
  data () {
    return {
      username: '',
      password: '',
      nickname: '',
    }
  },
  methods: {
    submitForm() {
      const formData = {
        username: this.username,
        password: this.password,
        nickname: this.nickname
      }
      axios
        .post(`${API_URL}/accounts/register/`, formData)
        .then(() => {
          alert('🎉회원가입에 성공하셨습니다🎉')
          this.$router.push('/login')
        })
        .catch((err) => {
          console.log(err.response);
          console.log(typeof(err.response.data))
          if (err.response.data.username !== 'undefined') {
            alert('이미 가입된 아이디입니다.')
          }
        });
    },
  }
};
</script>

<style>

</style>