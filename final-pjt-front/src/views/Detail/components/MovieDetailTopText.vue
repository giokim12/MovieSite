<template>
  <div class="text-slate-200">
    <div v-if="video" class="text-center fixed top-0 left-0 w-full h-full bg-opacity-60 bg-black" @click="video=false">
      <div id="ytplayer" class="text-center fixed top-36 left-[25%]"></div>
    </div>
    <div class="font-bold text-5xl">{{movie.title}}</div>
    <br>
    <div class="flex">
      <svg class="block h-8 w-8 text-red-500" fill="currentColor" xmlns="http://www.w3.org/2000/svg" viewBox="0 -5 20 24"><path d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"/></svg>
      <div class="font-bold text-2xl ml-1 mt-0.5">
        {{rate}}
        ({{comment.length}})
        •
        {{movie.released_date}}
      </div>
    </div>
    <br>
    <button @click="showModalMethod" class="bg-yellow-400 hover:bg-yellow-500 text-white font-bold py-2 px-4 border border-blue-700 rounded w-80 h-16">
      ▶ 트레일러
    </button>
    <!-- <MovieTrailerVue v-if="showModal" @close="showModal=false" :movieKey="key">
      <div slot="body">
        <div id="ytplayer"></div>
      </div>
    </MovieTrailerVue> -->
    <div class="font-bold text-1xl w-[500px] mt-4">
      {{movie.overview}}
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
// import MovieTrailerVue from './MovieTrailer.vue'
export default {
  name: 'MovieDetailTopText',
  data() {
    return {
      // showModal: false,
      video: false
    }
  },
  components: {
    // MovieTrailerVue
  },
  props: {
    movie:Object,
    comment:Object
  },
  computed: {
    rate() {
      let totalRate = 0
      let result = 0
      console.log(this.comment)
      if (this.comment.length > 0) {
        this.comment.forEach((el) => { totalRate += el.rate})
        result = (totalRate/this.comment.length).toFixed(1)
      }
      return result
    }
  },
  methods: {
    showModalMethod() {
      axios({
        method: 'GET',
        url: `${API_URL}/api/v1/detail/video/${this.$route.params.movie_id}`
      })
        .then((res) => {
          this.video=true
          return res
        })
        .then((res) => {
          onYouTubePlayerAPIReady(res.data[0].key)
        })
        .catch((err) => {
          console.log(err)
          
        })
    }
  }
}
let tag = document.createElement('script');
tag.src = "https://www.youtube.com/player_api";
let firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// Replace the 'ytplayer' element with an <iframe> and
// YouTube player after the API code downloads.
// eslint-disable-next-line
let player;
// eslint-disable-next-line
function onYouTubePlayerAPIReady(movieKey) {
  console.log('qkwpodkqwpodkp')
  // eslint-disable-next-line
  player = new YT.Player('ytplayer', {
    height: '860',
    width: '1200',
    videoId: movieKey,
    playerVars: {
        'rel': 0,    //연관동영상 표시여부(0:표시안함)
        'controls': 1,    //플레이어 컨트롤러 표시여부(0:표시안함)
        'autoplay' : 1,   //자동재생 여부(1:자동재생 함, mute와 함께 설정)
        'mute' : 0,   //음소거여부(1:음소거 함)
        'loop' : 1,    //반복재생여부(1:반복재생 함)
        'playsinline' : 1,    //iOS환경에서 전체화면으로 재생하지 않게
        'modestbranding' : 1
      },
  });
}
</script>

<style>
</style>