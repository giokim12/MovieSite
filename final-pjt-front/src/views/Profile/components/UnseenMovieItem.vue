<template>
  <div>
    <div  @mouseover="hover" @mouseout="hover" class="m-3 h-[90%] lg:hover:scale-110 lg:hover:rounded transition-transform ease-in-out duration-500 hover:cursor-pointer movie-card" >
      <!-- <div :class="isUnseen? '' : 'hidden'" class="text-white absolute top-40 left-10 h-[50%]"> 이제 이 영화는 추천되지 않습니다</div> -->
      <img @click="goDetail(), addView()" :class="isUnseen? 'opacity-25' : ''" class="w-[90%] h-[100%] rounded-xl" :src="imgPath" alt="..."/>
      <button 
        :class="isHover? 'visible' : 'invisible'" 
        class="text-white border bg-red-400 hover:bg-red-500 rounded-lg focus:ring-4 focus:outline-none p-1 focus:ring-red-200 absolute top-[85%] right-[35px]" 
        @click="cancelUnseen"
      >
        {{ isUnseenText }}
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name:'UnseenMovieItem',
  props: {
    movie: Object
  },
  data() {
    return{
      isHover: false,
      isUnseen: false,
      isUnseenText: '추천 받기'
    }
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
    cancelUnseen() {
      axios ({
        method: 'DELETE',
        url: `${API_URL}/api/v1/unseen/${this.movie.movie_id}/`,
        data: {
          user: this.$store.state.userdata.id,
          movie: this.movie.movie_id
        }
      })
        .then((res) => {
          console.log(res)

          this.isUnseen = false
          this.$emit('unseen')
        })
        .catch((err) => {
          console.log(err)
        })
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


.del-button-container {
  position: absolute;
  top: 0%;
  left: 0%;

}
.del-button {
  position: absolute;
  top: 90%;
  left: 70%;

}
</style>