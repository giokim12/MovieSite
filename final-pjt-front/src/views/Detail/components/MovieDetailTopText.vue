<template>
  <div class="text-slate-200">
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
    <button class="bg-yellow-400 hover:bg-yellow-500 text-white font-bold py-2 px-4 border border-blue-700 rounded w-80 h-16">
      ▶ 트레일러
    </button>
    <div class="font-bold text-1xl w-[500px] mt-4">
      {{movie.overview}}
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieDetailTopText',
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
  }
}
</script>

<style>
</style>