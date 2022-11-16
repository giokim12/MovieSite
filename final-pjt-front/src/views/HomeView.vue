<template>
  <div>
    <div>
      {{ intro }}
    </div>
    <br />
    <button>회원가입</button>
  </div>
</template>

<script>
export default {
  name: "HomeView",
  data() {
    return {
      intro: "안녕하세요 hello this is my homepage",
    };
  },
};
</script>

<style>
</style>