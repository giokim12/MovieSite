<template>
    <nav class="px-1 sm:px-4 rounded relative z-50">
      <div class="flex flex-wrap items-center justify-between mx-auto border-b-2 border-white px-20">
        <div>
          <router-link to="/main">
            <img class="w-15 h-10 mr-2 text-white my-2" src="../assets/small-logo.png" alt="">
          </router-link>
        </div>
        <div>
          <button v-if="isLogin" class="text-white mr-3">{{ nickname.nickname }} 님 환영합니다!</button>
        </div>
        <div>
          <router-link v-if="!isLogin" to="/signup" class="text-white mr-3">회원가입</router-link>
          <router-link v-if="!isLogin" to="/login" class="text-white rounded">로그인</router-link>
          <!-- <button v-if="isLogin" @click="logout" class="text-white mr-3 hover:underline">로그아웃</button>
          <router-link v-if="isLogin" to="/profile" class="text-white">내 프로필</router-link> -->
          <MainDropdownVue
            v-if="isLogin"
          >
            <template slot-scope="context">
              <button
                @click="context.toggleOpen"
                class="h-10 w-10 pl-0.5 cursor-pointer rounded text-white object-cover border-2"
              >
                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-list" viewBox="0 0 16 16">
                  <path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z"/>
                </svg>
              </button>
              <transition
                enter-active-class="transition-all duration-100 ease-out"
                leave-active-class="transition-all duration-100 ease-in"
                enter-class="opacity-0 scale-75"
                enter-to-class="opacity-100 scale-100"
                leave-class="opacity-100 scale-100"
                leave-to-class="opacity-0 scale-75"
              >
                <div
                  v-if="context.open"
                  class="origin-top-right absolute right-0 mt-0 w-32 bg-slate-900 border overflow-hidden rounded-lg shadow-md"
                >
                  <div class="p-2 hover:bg-slate-600">
                    <router-link to="/profile/unseen" class="text-white hover:no-underline">보기 싫은 영화</router-link>
                  </div>
                  <div class="p-2 hover:bg-slate-600">
                    <router-link to="/profile" class="text-white hover:no-underline">내 프로필</router-link>
                  </div>
                  <div class="p-2 hover:bg-slate-600 border-t-2 border-gray-500">
                    <button @click="logout" class="text-white">로그아웃</button>
                  </div>

                </div>
              </transition>
            </template>
          </MainDropdownVue>
        </div>
      </div>
    </nav>
</template>

<script>
// import axios from "axios";
// const API_URL = "http://127.0.0.1:8000";
import MainDropdownVue from './MainDropdown.vue'

export default {
  name: 'NavBar',
  components: {
    MainDropdownVue
  },
  computed: {
    isLogin() {
      return this.$store.state.access
    },
    nickname() {
      return this.$store.state.userdata
    }  
  },
  methods: {
    toggleOpen() {
      this.dropdown = !this.dropdown;
    },
    logout() {
      this.$store.commit('REMOVE_ACCESS');
      localStorage.setItem('access', '');
      localStorage.setItem('refresh', '');
      localStorage.setItem('vuex', '');
      this.$router.go()
    }
  }
}
</script>

<style>

</style>