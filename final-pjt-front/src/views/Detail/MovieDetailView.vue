<template>
  <div class="absolute inset-x-0 top-0 bg-black z-0">
    <div class="h-[1200px]">
      <div
        :style="{backgroundImage: `linear-gradient(to right, rgba(0, 0, 0, 0.95), rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.0)), url('${imgPath}')`}"
        class="top-0 h-full bg-cover bg-clip-content ml-96 rounded-tl-[50px] rounded-bl-[20%] top-back-img"
      > 
        <MovieDetailTopTextVue
          :movie="movie"
          :comment="get_comment"
          class="relative top-[200px] right-[300px]"
        />
      </div>
    </div>
    <br>
    <div class= "grid grid-cols-6 gap-4">
      <div class="col-span-4">
        <div class= " bg-red-100">
          <img class="h-96 w-full" :src="imgPath" alt="">
        </div>
        <div class="bg-red-500">
          <h1>출연진</h1>
          <div class="flex mr-3">
            <ActorList 
              v-for="(actor, idx) in actors"
              :key="idx"
              :actor = "actor"
            />
            <button class="bg-blue-500">></button>
          </div>
        </div>
        <div class= " bg-red-100">
          {{ movie?.overview }}
        </div>
      </div>
      <div class="col-span-2">
        <div class="bg-green-100">
          <CommentFormVue
            :movie= "movie"
          />
          <hr>
          <CommentListVue
            :movie= "movie"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
import ActorList from "@/views/Detail/components/ActorList";
import CommentFormVue from './components/CommentForm.vue';
import CommentListVue from './components/CommentList.vue';
import MovieDetailTopTextVue from './components/MovieDetailTopText.vue';


export default {
  name: "MovieDetailView",
  components: {
    ActorList,
    CommentFormVue,
    CommentListVue,
    MovieDetailTopTextVue,
  },
  data() {
    return {
      movie: null,
      actors: null,
    }
  },
  computed: {
    imgPath() {
      return "https://image.tmdb.org/t/p/original/"+this.movie?.backdrop_path
    },
    get_comment () {
      return this.$store.state.comments
    }
  },
  created() {
    this.getActorsbyMovie()
    this.getMovieDetail()
    this.getCommentList()
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'GET',
        url: `${API_URL}/api/v1/detail/${this.$route.params.movie_id}`
      })
        .then((res) => {
          this.movie = res.data
          console.log(res.data)
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
      this.$store.dispatch("getCommentList", this.$route.params.movie_id)
    }
  }
};
</script>

<style>
.top-back-img {
  box-shadow: 30px 2px 50px 50px black inset;
}
</style>
