<template>
  <div>
    <!-- <h4>한개의 영화</h4> -->
    <h5>{{ movie.title }}</h5>
  </div>
</template>

<script>
export default {
  name: "MovieListItem",
  props: {
    movie: Object
  }

}
</script>

<style>

</style>