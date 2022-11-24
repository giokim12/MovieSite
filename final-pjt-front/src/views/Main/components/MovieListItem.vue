<template>
  <div>
    <div @mouseover="hover" @mouseout="hover" class="m-3 lg:hover:scale-110 lg:hover:rounded transition-transform ease-in-out duration-500 hover:cursor-pointer relative" >
      <div :class="isUnseen? '' : 'hidden'" class="text-white absolute top-40 left-0 h-[50%]"> 이제 이 영화는 추천되지 않습니다</div>
      <img @click="goDetail(), addView()" :class="isUnseen? 'opacity-25' : ''" class="w-[90%] h-[35vh] rounded-xl" :src="imgPath" alt="..."/>
      <button 
        :class="isHover? 'visible' : 'invisible'" 
        v-if="isLogin" 
        class="text-white border bg-red-400 hover:bg-red-500 rounded-lg focus:ring-4 focus:outline-none p-1 focus:ring-red-200 absolute top-[87%] right-[35px]" 
        v-on="isUnseen ? {click:() => {cancelUnseen();}} : {click:() => {addUnseen();}}"
        
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
  name: "MovieListItem",
  data() {
    return{
      isHover: false,
      isUnseen: false,
      isUnseenText: '관심 없음'
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
      this.$router.push({ name: 'detail', params: { movie_id:this.movie.movie_id }}).catch(() => {})
      this.$router.go(this.$router.currentRoute)
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
    },
    addUnseen() {
      if (this.isLogin) {
        axios ({
          method: 'POST',
          url: `${API_URL}/api/v1/unseen/${this.movie.movie_id}/`,
          data: {
            user: this.$store.state.userdata.id,
            movie: this.movie.movie_id
          }
        })
          .then((res) => {
            console.log(res)
            this.isUnseen = true
            this.isUnseenText = '추천 받기'
          })
          .catch((err) => {
            console.log(err)
          })
      }
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
          this.isUnseenText = '관심 없음'
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


</style>