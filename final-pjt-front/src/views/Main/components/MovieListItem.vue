<template>
  <div>
    <div @mouseover="hover" @mouseout="hover" class="m-3 h-[100%] border border-white lg:hover:scale-110 lg:hover:rounded transition-transform ease-in-out duration-500 hover:cursor-pointer movie-card" @click="goDetail(), addView()">
      <!-- <div :style="{backgroundImage: `url('${imgPath}')`}"></div> -->
      <img class="w-[90%] h-[100%] rounded-xl hihi" :src="imgPath" alt="...">
      <div :class="isHover? 'visible' : 'invisible'" class="w-[90%] h-[100%] border border-red-700 del-button-container">
        <button :class="isHover? 'visible' : 'invisible'" class="text-white border border-white del-button ">
          <router-link to="/home" class="router-temp">{{ isHover }}</router-link>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "MovieListItem",
  data() {
    return{
      isHover: false
    }
  },
  props: {
    movie: Object
  },
  computed: {
    imgPath() {
      return "https://image.tmdb.org/t/p/original/"+this.movie.poster_path
    },
    isLogin() {
      return this.$store.state.access
    }
  },
  methods: {
    hover() {
      // alert(!this.isHover)
      this.isHover = !this.isHover
    },
    goDetail() {
      this.$router.push({ name: 'detail', params: { movie_id:this.movie.movie_id }})
    },
    addView() {
      if (this.isLogin) {
        axios ({
          method: 'POST',
          url: `${API_URL}/api/v1/detail/${this.movie.movie_id}/`,
          data: {
            user: this.$store.state.userdata.id,
            movie: this.movie.movie_id
          }
        })
          .then((res) => {
            console.log(res)
          })
          .catch((err) => {
            console.log(err)
          })
      }
    }
  },
}
</script>

<style>
.overview {
  display:-webkit-box; 
  word-wrap:break-word; 
  -webkit-line-clamp:4; 
  -webkit-box-orient:vertical; 
  overflow:hidden; 
  text-overflow:ellipsis;
}

.movie-card {
  /* background-image: :src="imgPath"; */
  position: relative;


}

.hihi {

}

.del-button-container {
  position: absolute;
  top: 0%;
  left: 0%;

}
.del-button {
  position: absolute;
  top: 80%;
  left: 70%;

}

.router-temp {

}
</style>