<template>
  <div>
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

export default {
  name: "MovieDetailView",
  components: {
    ActorList,
    CommentFormVue,
    CommentListVue,
  },
  data() {
    return {
      movie: null,
      actors: null,
    }
  },
  computed: {
    imgPath() {
      return "https://image.tmdb.org/t/p/original/"+this.movie?.poster_path
    }
  },
  created() {
    this.getActorsbyMovie()
    this.getMovieDetial()
  },
  methods: {
    getMovieDetial() {
      axios({
        method: 'GET',
        url: `${API_URL}/api/v1/movies/${this.$route.params.movie_id}`
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
    }
  }
};
</script>

<style>
</style>
