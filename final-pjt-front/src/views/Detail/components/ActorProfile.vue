<template>
  <div class="profile text-center text-black w-[90%] h-[460px] m-3">
    <div class="avatar">
      <img class="photo mx-auto w-[200px] h-[200px] xl:h-[300px] xl:w-[300px]" :src="'https://image.tmdb.org/t/p/original'+actor.profile_path" alt="">
      <span class='p-2 new bg-[#F2DB68] hover:bg-[#09D05F] hover:cursor-pointer' @click="search(actor.name)">
        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
          <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
        </svg>
      </span>
    </div>
    <h1>{{actor.name}}</h1>
    <p class="text-2xl font-bold">{{actor.character}}</p>
  </div>
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
  left: 80%;
  top: 10%;
  /* background-color: aquamarine; */
  padding: 0.2rem 0.5rem;
  border-radius: 0.5rem;
  text-transform: uppercase;
  font-weight: bold;
}

</style>
