<template>
  <div class="profile text-center text-black w-[90%] h-[460px] m-3">
    <div class="avatar">
      <img class="photo mx-auto w-[200px] h-[200px] xl:h-[300px] xl:w-[300px]" :src="'https://image.tmdb.org/t/p/original'+actor.profile_path" alt="">
      <span class='new bg-emerald-200 hover:bg-emerald-400 hover:cursor-pointer' @click="search(actor.name)">More</span>
    </div>
    <h1>{{actor.name}}</h1>
    <p class="text-2xl font-bold">{{actor.character}}</p>
  </div>
<!-- <div class="no-underline rounded border border-white m-3 text-center text-xl h-{800px} w-{500px} md:h-{1200px} md:w-{800px}">
      <div class="text-center h-[120px] pt-3">
        <div class="text-3xl">{{ actor.name }}</div>
        <div class="text-2xl mb-2">{{ actor.character }}</div>
      </div>
      <img :src="'https://image.tmdb.org/t/p/original'+actor.profile_path" class="rounded h-full w-full" alt="">
      <div @click="search(actor.name)">detail</div>
    </div> -->
</template>

<script>

export default {
  name: "ActorProfile",
  data() {
    return {
    }
  },
  props: {
    actor: Object
  },
  methods: {
    search(name) {
      window.open('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query='+name)
    }
  }
  
};
</script>

<style>
.orange {
  color: orange;
}

.profile {
  /* height: 350px; */
  /* width: 300px; */
  /* text-align: center; */
  padding: 1rem;
  background-color: #ebebeb;
  border-radius: 20px;
  box-shadow: 7px 5px 23px -9px rgba(199, 190, 190, 0.75);
  margin-bottom: 1rem;
  -webkit-box-shadow: 7px 5px 23px -9px rgba(196, 178, 178, 0.75);
  -moz-box-shadow: 7px 5px 23px -9px rgba(192, 171, 171, 0.75);
}

.photo {
  /* width: 200px;
  height: 200px; */
  border-radius: 100%;
}

.avatar {
  position: relative;
  width: 300px;
  height: 300px;
  margin: auto;
}

.new {
  position: absolute;
  left: 73%;
  top: 10%;
  /* background-color: aquamarine; */
  padding: 0.2rem 0.5rem;
  border-radius: 0.5rem;
  text-transform: uppercase;
  font-weight: bold;
}

</style>
