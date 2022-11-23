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
                class="h-10 w-32 cursor-pointer rounded-full text-white object-cover"
              >
                마이페이지
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
                  class="origin-top-right absolute right-0 mt-2 w-32 bg-white border overflow-hidden rounded-lg shadow-md"
                >
                  <ul>
                    <li class="hover:bg-gray-100 h-10 border-b-2">
                      <router-link to="/profile/unseen" class="text-black">보기 싫은 영화</router-link>
                    </li>
                    <li class="hover:bg-gray-100">
                      <router-link to="/profile" class="text-black">내 프로필</router-link>
                    </li>
                    <li class="hover:bg-gray-100">
                      <button @click="logout" class="mr-3 hover:underline">로그아웃</button>
                    </li>
                  </ul>
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