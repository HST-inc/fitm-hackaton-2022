<template>
  <HelloWorld v-bind:msg="msg"/>
</template>

<script setup lang="ts">
  import { ref } from 'vue';
  import HelloWorld from './components/HelloWorld.vue';

  const msg = ref(import.meta.env.VITE_SOME_KEY);
</script>

<style scoped>
  .logo {
      height: 6em;
      padding: 1.5em;
      will-change: filter;
  }
  .logo:hover {
      filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.vue:hover {
      filter: drop-shadow(0 0 2em #42b883aa);
  }
</style>
