<template>
  <div>
      <h2 class="text-white">투표 내림차순 정렬</h2>
      <div class="w-full h-full">
        <Carousel class="text-white ml-4" :per-page="6" paginationColor="white" paginationActiveColor="#FF3471" :centerMode=true :autoplay=true :loop=true :autoplayTimeout=6000>
          <slide
            v-for = "(movie, idx) in movies_voted"
            :key = "`movie${idx}`"
            :movie = "movie"
            class="h-full"
          >
            <MovieListItem :movie = "movie"/>
          </slide>
        </Carousel>
      </div>
      <hr>
      <h2 class="text-white">인기도 내림차순 정렬</h2>
      <div class="w-full h-full">
        <Carousel class="text-white ml-4" :per-page="6" paginationColor="white" paginationActiveColor="#FF3471" :centerMode=true :autoplay=true :loop=true :autoplayTimeout=6000>
          <slide
            v-for = "(movie, idx) in movies_popular"
            :key = "`movie${idx}`"
            :movie = "movie"
            class="h-full"
          >
            <MovieListItem :movie = "movie"/>
          </slide>
        </Carousel>
      </div>
      <hr>
      <h2 class="text-white">고전명작</h2>
      <div class="w-full h-full">
        <Carousel class="text-white ml-4" :per-page="6" paginationColor="white" paginationActiveColor="#FF3471" :centerMode=true :autoplay=true :loop=true :autoplayTimeout=6000>
          <slide
            v-for = "(movie, idx) in movies_old"
            :key = "`movie${idx}`"
            :movie = "movie"
            class="h-full"
          >
            <MovieListItem :movie = "movie"/>
          </slide>
        </Carousel>
      </div>
      <hr>
    <div
      v-if="isLogin"
    >
      <hr>
      <h2 class="text-white">클릭한거</h2>
      <div class="flex">
        <MovieListItem
          v-for = "(movie, idx) in movies_clicked"
          :key = "idx"
          :movie = "movie"
          class="flex"
        />
      </div>
    </div>
    <hr>
    <h2 class="text-white">장르같은거</h2>
    <div class="flex">
      <MovieListItem
        v-for = "(movie, idx) in movies_algo_genre"
        :key = "idx"
        :movie = "movie"
        class="flex"
      />
    </div>
    <hr>
    <h2 class="text-white">유클리디안 거리</h2>
    <div class="flex">
      <MovieListItem
        v-for = "(movie, idx) in movies_algo_euc"
        :key = "idx"
        :movie = "movie"
        class="flex"
      />
    </div>
    <hr>
    <h2 class="text-white">개인 유명영화</h2>
    <div class="flex">
      <MovieListItem
        v-for = "(movie, idx) in movies_algo_popular"
        :key = "idx"
        :movie = "movie"
        class="flex"
      />
    </div>
    <hr>
    <h2 class="text-white">개인 고전영화</h2>
    <div class="flex">
      <MovieListItem
        v-for = "(movie, idx) in movies_algo_old"
        :key = "idx"
        :movie = "movie"
        class="flex"
      />
    </div>
    <hr>
    <h2 class="text-white">개인 투표영화</h2>
    <div class="flex">
      <MovieListItem
        v-for = "(movie, idx) in movies_algo_voted"
        :key = "idx"
        :movie = "movie"
        class="flex"
      />
    </div>
  </div>


</template>

<script>
import MovieListItem from '@/views/Main/components/MovieListItem'
import { Carousel, Slide } from 'vue-carousel';

export default {
  name: "PopularMovieList",
  components: {
    MovieListItem,
    Carousel,
    Slide
  },
  computed: {
    isLogin() {
      return this.$store.state.access
    },
    movies_voted () {
      return this.$store.state.moviesVoted
    },
    movies_popular () {
      return this.$store.state.moviesPopular
    },
    movies_old () {
      return this.$store.state.moviesOld
    },
    movies_clicked () {
      return this.$store.state.moviesClicked
    },
    movies_algo_genre() {
      return this.$store.state.moviesAlgoGenre
    },
    movies_algo_euc() {
      return this.$store.state.moviesAlgoEuc
    },
    movies_algo_popular() {
      return this.$store.state.moviesAlgoPopular
    },
    movies_algo_old() {
      return this.$store.state.moviesAlgoOld
    },
    movies_algo_voted() {
      return this.$store.state.moviesAlgoVoted
    },
  }
}


</script>

<style>

</style>