<template>
  <div class="homeview-div">
    <div class="text-white">
      dqqdw
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeView",
};
</script>

<style>
.homeview-div{
  position: relative;
  height: 100vh;
  opacity: 0.9;
}
.homeview-div:after{
  content : "";
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  background-image: url('../assets/jwt-bg.png');
  background-size: cover;
  width: 100%;
  height: 100%;
  opacity : 0.2;
  z-index: -1;
}
</style>