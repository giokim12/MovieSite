<template>
  <div class="profile-div">
    <section class="bg-black bg-opacity-75 h-screen">
      <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-full lg:py-0">
        <div class="w-full rounded-xl shadow dark:border md:mt-0 sm:max-w-md xl:p-2 opacity-100">
          <div class="p-6 space-y-4 md:space-y-6 sm:p-8 bg-black rounded-xl border border-white">
            <h1 class="text-xl font-bold leading-tight tracking-tight text-white md:text-2xl">
              내 프로필
            </h1>
            <div class="flex items-center mt-8 mb-4 ml-4">
                <img class="w-80 h-60 mr-2 text-white" src="../../assets/logo.png" alt="logo">  
            </div>
            <form class="rounded-2xl pl-3 space-y-4 md:space-y-6 pb-10" v-on:submit.prevent="nicknameForm">
              <div class="flex items-center mt-8 mb-4">
                  <!-- <label for="username" class="block mb-2 text-sm font-medium text-white">아이디</label> -->
                  <input v-model="nickname" type="text" name="nickname" id="nickname" :placeholder="this.$store.state.userdata.nickname" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-75 p-2.5">
                  <button type="submit" class="text-white bg-red-400 hover:bg-red-500 focus:ring-4 focus:outline-none focus:ring-red-200 font-medium rounded-lg text-sm w-25 p-2.5 mx-6 text-center">수정하기</button>
              </div>
            </form>
            <!-- <div>
              <button @click="unseenList()" class="text-white bg-yellow-400 hover:bg-yellow-500 focus:ring-4 focus:outline-none focus:ring-yellow-200 font-medium rounded-lg text-sm mr-5 px-5 py-2.5 mb-10 text-center">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-bookmark-x" viewBox="0 0 16 16">
                  <path fill-rule="evenodd" d="M6.146 5.146a.5.5 0 0 1 .708 0L8 6.293l1.146-1.147a.5.5 0 1 1 .708.708L8.707 7l1.147 1.146a.5.5 0 0 1-.708.708L8 7.707 6.854 8.854a.5.5 0 1 1-.708-.708L7.293 7 6.146 5.854a.5.5 0 0 1 0-.708z"/>
                  <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z"/>
                </svg>
              </button>
            </div> -->
            <div class="flex flex-row-reverse">
              <!-- <button class="text-white bg-red-400 hover:bg-red-500 focus:ring-4 focus:outline-none focus:ring-red-200 font-medium rounded-lg text-sm mr-6 px-3 py-2.5 text-center">적용하기</button> -->
              <button class=" text-white bg-red-400 hover:bg-red-500 focus:ring-4 focus:outline-none focus:ring-red-200 font-medium rounded-lg text-sm px-3 py-2.5 text-center">
                <router-link to="/main" class="text-white">메인으로 돌아가기</router-link>
              </button>
            </div>
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
  name: "MyProfileView",
  data() {
    return {
      nickname: '',
    }
  },
  // computed: {
  //   movies_unseen() {
  //     return this.$store.state.moviesUnseen
  //   },
  // },
  created() {
    // this.getUnseenMovies()
    this.isLogin()
  },
  methods: {
    isLogin() {
      if (!this.$store.state.userdata) {
        this.$router.push({ name: 'login'})
      }
    },
    nicknameForm() {
      axios({
        method: 'put',
        url: `${API_URL}/api/v1/auth/users/me/`,
          headers: {
            Authorization: `Bearer ${this.$store.state.access}`
          },
          data: {
            username: this.$store.state.userdata.username,
            nickname: this.nickname,
            password: this.$store.state.userdata.password,
            id: this.$store.state.userdata.id
          }
        })
        .then((res) => {
          this.$store.commit('GET_ME', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    // getUnseenMovies() {
    //   this.$store.dispatch("getUnseenMovies", this.$store.state.userdata.id);
    // },
    // unseenList() {
    //   // alert('qwdqw')
    //   this.$router.push({ name: 'unseen'})
    // },
  }
};
</script>

<style>
.profile-div{
  content : "";
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  background-image: url('../../assets/jwt-bg.png');
  background-size: cover;
  width: 100%;
  height: 100%;
  /* opacity : 0.2; */
  z-index: -1;
}
</style>