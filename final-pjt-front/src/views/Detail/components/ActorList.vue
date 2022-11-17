<template>
  <div>
    <h2>나는 배우들</h2>
    <ActorListItem 
      v-for="(actor, idx) in actors" 
      :key="idx" 
      :actor="actor" 
    />
  </div>
</template>

<script>
import ActorListItem from "@/views/Detail/components/ActorListItem";

export default {
  name: "ActorList",
  components: {
    ActorListItem,
  },
  computed: {
    actors() {
      return this.$store.state.actors
    }
  }
};
</script>

<style></style>
