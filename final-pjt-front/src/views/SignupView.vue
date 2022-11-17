<template>
  <div>
    <!-- <h1>sign up</h1>
    <form v-on:submit.prevent="submitForm">
      <label for="username">Username</label>
      <input type="text" name="username" v-model="username">
      <label for="password">Username</label>
      <input type="password" name="password" v-model="password">
    </form> -->
    <section class="bg-gray-50">
      <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
        <a href="#" class="flex items-center mb-6 text-2xl font-semibold text-gray-900">
            <img class="w-8 h-8 mr-2" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/logo.svg" alt="logo">
            Flowbite    
        </a>
        <div class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0">
          <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
              <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl">
                Create and account
              </h1>
              <form class="space-y-4 md:space-y-6" v-on:submit.prevent="submitForm">
                  <div>
                      <label for="username" class="block mb-2 text-sm font-medium text-gray-900">Your username</label>
                      <input v-model="username" type="text" name="username" id="username" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5" required="">
                  </div>
                  <div>
                      <label for="nickname" class="block mb-2 text-sm font-medium text-gray-900">Your nickname</label>
                      <input v-model="nickname" type="text" name="nickname" id="nickname" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5" required="">
                  </div>
                  <div>
                      <label for="password" class="block mb-2 text-sm font-medium text-gray-900">Password</label>
                      <input v-model="password" type="password" name="password" id="password" placeholder="••••••••" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5" required="">
                  </div>
                  <button type="submit" class="w-full text-white bg-cyan-600 hover:bg-cyan-700 focus:ring-4 focus:outline-none focus:ring-cyan-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center">Sign up</button>
                  <p class="text-sm font-light text-gray-500">
                    Already have an account? <a href="#" class="font-medium text-cyan-600 hover:underline">Sign in</a>
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
        .then((res) => {
          console.log(res)
          this.$router.push('/')
        })
        .catch((err) => {
          console.log(err);
        });
    },
  }
};
</script>

<style>

</style>