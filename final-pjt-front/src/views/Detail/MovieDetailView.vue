<template>
  <div class="absolute inset-x-0 top-0 bg-black z-0">
    <div class="h-[1000px]">
      <div
        :style="{backgroundImage: `linear-gradient(to right, rgba(0, 0, 0, 0.95), rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.0)), url('${imgPath}')`}"
        class="top-0 h-full bg-cover bg-clip-content ml-96 rounded-tl-[50px] rounded-bl-[20%] top-back-img"
      > 
        <MovieDetailTopTextVue
          :movie="movie"
          :comment="get_comment"
          :actors="actors"
          class="relative top-[200px] right-[300px]"
        />
      </div>
    </div>
    <div class="flex flex-wrap">
      <div class="w-full">
        <div class="border-b-2 border-[#808078]">
          <ul class="flex mb-0 w-[500px] list-none flex-wrap flex-row">
            <li class="-mb-px mr-2 last:mr-0 flex-auto hover:cursor-pointer text-center">
              <a class="text-xl bg-black font-bold uppercase px-5 py-3 shadow-lg block hover:text-white leading-normal" v-on:click="toggleTabs(1)" v-bind:class="{'text-[#808078]': openTab !== 1, 'text-white border-b-4 border-white': openTab === 1}">
                코멘트
              </a>
            </li>
            <li class="-mb-px mr-2 last:mr-0 flex-auto hover:cursor-pointer text-center">
              <a class="text-xl bg-black font-bold uppercase px-5 py-3 shadow-lg block hover:text-white leading-normal" v-on:click="toggleTabs(2)" v-bind:class="{'text-[#808078]': openTab !== 2, 'text-white border-b-4 border-white': openTab === 2}">
                출연진
              </a>
            </li>
            <li class="-mb-px mr-2 last:mr-0 flex-auto hover:cursor-pointer text-center">
              <a class="text-xl bg-black font-bold uppercase px-5 py-3 shadow-lg block hover:text-white leading-normal" v-on:click="toggleTabs(3)" v-bind:class="{'text-[#808078]': openTab !== 3, 'text-white border-b-4 border-white': openTab === 3}">
                영화
              </a>
            </li>
          </ul>
        </div>
        <div class="relative flex flex-col min-w-0 break-words w-full mb-3 shadow-lg rounded">
          <div class="px-5 py-5 flex-auto">
            <div class="tab-content tab-space">
              <div v-bind:class="{'hidden': openTab !== 1, 'block': openTab === 1}" class="text-white flex">
                <CommentStarsVue
                  :comment="get_comment"
                  :movie="movie"
                  class="mr-5 min-w-96"
                >
                </CommentStarsVue>
                <CommentListVue
                  :movie= "movie"
                  class="ml-5 w-full"
                />
                <!-- <CommentCreateVue
                  :movie= "movie"
                  class="border border-white">
                ></CommentCreateVue> -->
              </div>
              <div class="actors" v-bind:class="{'hidden': openTab !== 2, 'block': openTab === 2}">
                <Carousel :per-page="5" paginationColor="white" paginationActiveColor="#FF3471" class="text-white">
                  <slide 
                    v-for="actor in actors"
                    :key="actor.person_id"
                    class=""
                  >
                    <ActorProfile
                      :actor="actor"
                    />
                  </slide>
                </Carousel>
              </div>
              <div v-bind:class="{'hidden': openTab !== 3, 'block': openTab === 3}" >
                <h2 class="text-white">🍿이런 영화는 어떠세요?🍿</h2>
                  <SimilarMovieList/>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
import ActorProfile from "@/views/Detail/components/ActorProfile";
import CommentStarsVue from './components/CommentStars.vue';
// import CommentCreateVue from './components/CommentCreate.vue';
import CommentListVue from './components/CommentList.vue';
import MovieDetailTopTextVue from './components/MovieDetailTopText.vue';
import { Carousel, Slide } from 'vue-carousel';
import SimilarMovieList from './components/SimilarMovieList.vue';

export default {
  name: "MovieDetailView",
  components: {
    // ActorList,
    // CommentCreateVue,
    CommentListVue,
    CommentStarsVue,
    ActorProfile,
    MovieDetailTopTextVue,
    Carousel,
    Slide,
    SimilarMovieList,
  },
  data() {
    return {
      movie: null,
      actors: null,
      openTab: 1
    }
  },
  computed: {
    imgPath() {
      return "https://image.tmdb.org/t/p/original/"+this.movie?.backdrop_path
    },
    posterPath() {
      return "https://image.tmdb.org/t/p/original/"+this.movie?.poster_path
    },
    get_comment () {
      return this.$store.state.comments
    },
  },
  created() {
    this.getActorsbyMovie()
    this.getMovieDetail()
    this.getCommentList()
    this.getSimilar() 
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'GET',
        url: `${API_URL}/api/v1/detail/${this.$route.params.movie_id}`
      })
        .then((res) => {
          this.movie = res.data
          // console.log(res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getActorsbyMovie() {
      axios({
        method: 'GET',
        url: `${API_URL}/api/v1/movies/actors/${this.$route.params.movie_id}`
      })
        .then((res) => {
          this.actors = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getCommentList() {
      this.$store.dispatch({
        type: "getCommentList",
        movie_id: this.$route.params.movie_id, 
        sort: 'NEW'
      })
    },
    toggleTabs: function(tabNumber){
      this.openTab = tabNumber
    },
    search(name) {
      window.open('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query='+name)
    },
    getSimilar() {
      this.$store.dispatch("getSimilarMovies", this.$route.params.movie_id);
    }
  },
};
</script>
<!-- <script src="../../assets/actors.js"></script> -->
<style>
.top-back-img {
  box-shadow: 30px 2px 50px 50px black inset;
}
/* @import "../../assets/actors.css"; */
</style>
