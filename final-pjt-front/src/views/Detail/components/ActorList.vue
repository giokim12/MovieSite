<template>
    <div>
    </div>
</template>

<script>

export default {
  name: "ActorList",
  data() {
    return {
    }
  },
  props: {
    actors: Object
  },
  computed: {
    imgPath() {
      // console.log(this.actor?.profile_path)
      return "https://image.tmdb.org/t/p/original"+this.actor?.profile_path
    }
  },
};
</script>

<style>
</style>
