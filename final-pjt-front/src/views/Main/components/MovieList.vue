<template>
  <div>
    <div
      v-if="!isLogin"
    >
      <hr>
      <h2 class="text-white">πΏν μ΄μ©μλ€μ΄ κ·Ήμ°¬ν μνπΏ</h2>
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
      <h2 class="text-white">πΏμμ¦ ν«ν μνπΏ</h2>
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
      <h2 class="text-white">πΏκ³ μ  λͺμπΏ</h2>
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
    <!-- μ¬κΈ°μλΆν°λ λ‘κ·ΈμΈ ν΄μΌμ§ λλκ±° -->
    <div
      v-if="isLogin"
    >
    <hr>
    <h3 v-if="!movies_clicked.length" class=" text-white ml-4 pl-2">πμνλ₯Ό ν΄λ¦­ν΄λ³΄μΈμ.π</h3>
    <h3 v-if="!movies_clicked.length" class=" text-white ml-4 pl-2">μκ³ λ¦¬μ¦μ΄ μ¬λ¬λΆμκ² λ± λ§λ μνλ₯Ό μΆμ²ν΄λλ¦½λλ€π¬</h3>
      <div v-if="movies_algo_euc.length" >
        <hr>
        <h2 class=" text-white ml-4 pl-2">πΏμ ν΄λ¦¬λμ κ±°λ¦¬ κΈ°λ° μκ³ λ¦¬μ¦ μΆμ² μνπΏ</h2>
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
            <h3 class=" text-white ml-4 pt-3 pl-4">μκ³ λ¦¬μ¦ κΈ°λ° μν μΆμ²μ μνμ λ€λ©΄ μνλ₯Ό νμν΄μ£ΌμΈμ</h3>
          </div> -->
        </div>
      </div>
      <hr>
      <h2 class="text-white ml-4 pl-2">πΏμμ¦ ν«ν μνπΏ</h2>
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
      <h2 class="text-white ml-4 pl-2">πΏκ³ μ  λͺμπΏ</h2>
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
      <h2 class="text-white ml-4 pl-2">πΏν μ΄μ©μλ€μ΄ κ·Ήμ°¬ν μνπΏ</h2>
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
        <h2 class="text-white ml-4 pl-2">πΏμ₯λ₯΄ κΈ°λ° μΆμ² μνπΏ</h2>
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
            <h3 class=" text-white ml-4 pt-3 pl-4">μκ³ λ¦¬μ¦ κΈ°λ° μν μΆμ²μ μνμ λ€λ©΄ μνλ₯Ό νμν΄μ£ΌμΈμ</h3>
          </div> -->
        </div>
      </div>
      <hr>
      <h2 class="text-white ml-4 pl-2">πΏμ΅κ·Ό λ΄κ° λ³Έ μνπΏ</h2>
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
          <h3 class=" text-white ml-4 py-3 pl-4">μμ§ λ³Έ μνκ° μμ΄μ!</h3>
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