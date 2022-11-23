<template>
  <div class="flex justify-center">
    <div class="relative">
      <div v-if="navdrop" @click="navdrop = false" class="fixed inset-0"></div>
      <slot :open="navdrop" :toggleOpen="toggleOpen"></slot>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      navdrop: false
    };
  },
  methods: {
    toggleOpen() {
      this.navdrop = !this.navdrop;
    }
  }
};
</script>