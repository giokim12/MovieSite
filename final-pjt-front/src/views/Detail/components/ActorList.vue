<template>
  <div class="mr-3">
    <img :src="imgPath" alt="" class="rounded-xl w-32"/>
    <!-- <div>{{ actor?.name }}</div> -->
  </div>
</template>

<script>

export default {
  name: "ActorList",
  props: {
    actor: Object
  },
  computed: {
    imgPath() {
      // console.log(this.actor?.profile_path)
      return "https://image.tmdb.org/t/p/original"+this.actor?.profile_path
    }
  }
};
</script>

<style></style>
