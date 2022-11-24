<template>
  <div>
    <div
      v-if="!isLogin"
    >
      <hr>
      <h2 class="text-white">🍿타 이용자들이 극찬한 영화🍿</h2>
      <div class="w-full h-full">
        <Carousel class="text-white ml-4" :per-page="2" :perPageCustom="[[576, 3], [768, 4], [768, 5], [1200, 6]]" paginationColor="white" paginationActiveColor="#FF3471" :centerMode=true :autoplay=true :loop=true :autoplayTimeout=6000>
          <slide
            v-for = "(movie, idx) in movies_voted"
            :key = "`movie${idx}`"
            :movie = "movie"
          >
            <MovieListItem :movie = "movie"/>
          </slide>
        </Carousel>
      </div>
      <hr>
      <h2 class="text-white">🍿요즘 핫한 영화🍿</h2>
      <div class="w-full h-full">
        <Carousel class="text-white ml-4" :per-page="2" :perPageCustom="[[576, 3], [768, 4], [768, 5], [1200, 6]]" paginationColor="white" paginationActiveColor="#FF3471" :centerMode=true :autoplay=true :loop=true :autoplayTimeout=6000>
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
      <h2 class="text-white">🍿고전 명작🍿</h2>
      <div class="w-full h-full">
        <Carousel class="text-white ml-4" :per-page="2" :perPageCustom="[[576, 3], [768, 4], [768, 5], [1200, 6]]" paginationColor="white" paginationActiveColor="#FF3471" :centerMode=true :autoplay=true :loop=true :autoplayTimeout=6000>
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
    </div>
    <!-- 여기서부터는 로그인 해야지 되는거 -->
    <div
      v-if="isLogin"
    >
    <hr>
    <h3 v-if="!movies_clicked.length" class=" text-white ml-4 pl-2">🎞영화를 클릭해보세요.🎞</h3>
    <h3 v-if="!movies_clicked.length" class=" text-white ml-4 pl-2">알고리즘이 여러분에게 딱 맞는 영화를 추천해드립니다🎬</h3>
      <div v-if="movies_algo_euc.length" >
        <hr>
        <h2 class=" text-white ml-4 pl-2">🍿유클리디안 거리 기반 알고리즘 추천 영화🍿</h2>
        <div class="w-full h-full">
          <Carousel class="text-white ml-4" :per-page="2" :perPageCustom="[[576, 3], [768, 4], [768, 5], [1200, 6]]" paginationColor="white" paginationActiveColor="#FF3471" :centerMode=true :autoplay=true :loop=true :autoplayTimeout=6000>
            <slide
              v-for = "(movie, idx) in movies_algo_euc"
              :key = "`movie${idx}`"
              :movie = "movie"
              class="h-full"
              
            >
              <MovieListItem :movie = "movie"/>
            </slide>
          </Carousel>
          <!-- <div v-else>
            <h3 class=" text-white ml-4 pt-3 pl-4">알고리즘 기반 영화 추천을 원하신다면 영화를 탐색해주세요</h3>
          </div> -->
        </div>
      </div>
      <hr>
      <h2 class="text-white ml-4 pl-2">🍿요즘 핫한 영화🍿</h2>
      <div class="w-full h-full">
        <Carousel class="text-white ml-4" :per-page="2" :perPageCustom="[[576, 3], [768, 4], [768, 5], [1200, 6]]" paginationColor="white" paginationActiveColor="#FF3471" :centerMode=true :autoplay=true :loop=true :autoplayTimeout=6000>
          <slide
            v-for = "(movie, idx) in movies_algo_popular"
            :key = "`movie${idx}`"
            :movie = "movie"
            class="h-full"
          >
            <MovieListItem :movie = "movie"/>
          </slide>
        </Carousel>
      </div>
      <hr>
      <h2 class="text-white ml-4 pl-2">🍿고전 명작🍿</h2>
      <div class="w-full h-full">
        <Carousel class="text-white ml-4" :per-page="2" :perPageCustom="[[576, 3], [768, 4], [768, 5], [1200, 6]]" paginationColor="white" paginationActiveColor="#FF3471" :centerMode=true :autoplay=true :loop=true :autoplayTimeout=6000>
          <slide
            v-for = "(movie, idx) in movies_algo_old"
            :key = "`movie${idx}`"
            :movie = "movie"
            class="h-full"
          >
            <MovieListItem :movie = "movie"/>
          </slide>
        </Carousel>
      </div>
      <hr>
      <h2 class="text-white ml-4 pl-2">🍿타 이용자들이 극찬한 영화🍿</h2>
      <div class="w-full h-full">
        <Carousel class="text-white ml-4" :per-page="2" :perPageCustom="[[576, 3], [768, 4], [768, 5], [1200, 6]]" paginationColor="white" paginationActiveColor="#FF3471" :centerMode=true :autoplay=true :loop=true :autoplayTimeout=6000>
          <slide
            v-for = "(movie, idx) in movies_algo_voted"
            :key = "`movie${idx}`"
            :movie = "movie"
            class="h-full"
          >
            <MovieListItem :movie = "movie"/>
          </slide>
        </Carousel>
      </div>
      <div v-if="movies_algo_genre.length">
        <hr>
        <h2 class="text-white ml-4 pl-2">🍿장르 기반 추천 영화🍿</h2>
        <div class="w-full h-full">
          <Carousel  class="text-white ml-4" :per-page="2" :perPageCustom="[[576, 3], [768, 4], [768, 5], [1200, 6]]" paginationColor="white" paginationActiveColor="#FF3471" :centerMode=true :autoplay=true :loop=true :autoplayTimeout=6000>
            <slide
              v-for = "(movie, idx) in movies_algo_genre"
              :key = "`movie${idx}`"
              :movie = "movie"
              class="h-full"
            >
              <MovieListItem :movie = "movie"/>
            </slide>
          </Carousel>
          <!-- <div v-else>
            <h3 class=" text-white ml-4 pt-3 pl-4">알고리즘 기반 영화 추천을 원하신다면 영화를 탐색해주세요</h3>
          </div> -->
        </div>
      </div>
      <hr>
      <h2 class="text-white ml-4 pl-2">🍿최근 내가 본 영화🍿</h2>
      <div class="w-full h-full">
        <Carousel  v-if="movies_clicked.length" class="text-white ml-4" :per-page="2" :perPageCustom="[[576, 3], [768, 4], [768, 5], [1200, 6]]" paginationColor="white" paginationActiveColor="#FF3471" :centerMode=true :autoplay=true :loop=true :autoplayTimeout=6000>
          <slide
            v-for = "(movie, idx) in movies_clicked"
            :key = "`movie${idx}`"
            :movie = "movie"
            class="h-full"
          >
            <MovieListItem :movie = "movie"/>
          </slide>
        </Carousel>
        <div v-else>
          <h3 class=" text-white ml-4 py-3 pl-4">아직 본 영화가 없어요!</h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieListItem from '@/views/Main/components/MovieListItem'
import { Carousel, Slide } from 'vue-carousel';

export default {
  name: "MovieList",
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