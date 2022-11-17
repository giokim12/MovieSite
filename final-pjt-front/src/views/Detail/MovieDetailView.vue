<template>
  <div>
    <div class= "grid grid-rows-6 grid-cols-4 gap-4 lg:gap-6">
      <div class= "grid row-span-4 col-span-3 bg-red-100">영화</div>
      <div class= "grid col-span-1 row-span-6 bg-green-100">댓글이랑 좋아요랑</div>
      <div class= "grid col-span-3 bg-red-100"><ActorList /></div>
      <div class= "grid col-span-3 bg-red-100">영화 설명</div>
    </div>
  </div>
</template>

<script>
import ActorList from "@/views/Detail/components/ActorList";

export default {
  name: "MovieDetailView",
  components: {
    ActorList,
  },
  data() {
    return {
      actor: []
    }
  },
  computed: {
    actors() {
      return this.$store.state.actors
    }
  },
  created() {
    this.getActors()
  },
  methods: {
    getActorsbyMovie() {
      const movie_id = this.$route.params.movie_id
      for (const actor of this.actors) {
        if (actor.movie_id === Number(movie_id)) {
          this.actor = actor
          break
        }
      }
      // this.$store.dispatch('getActors')
    }
  }
};
</script>

<style>
</style>
