<template>
  <div>
    <div>
      {{ intro }}
    </div>
    <br />
    <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">회원가입</button>
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