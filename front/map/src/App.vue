<script setup>
import BottomMenu from './components/BottomMenu.vue'
import BackgroundMap from './components/BackgroundMap.vue'
import Getmac from './components/GetMac.vue'
import { onMounted, ref } from 'vue';

const is_init = ref(false);

onMounted(() => {
  if (localStorage.getItem('mac') !== null) {
    // is_init.value = true;
  }
});

</script>

<template>
  <BackgroundMap />
  <BottomMenu />
  <Getmac v-if="!is_init" />
  <!--<div id="log" style="color: white;">0</div> -->
</template>

<style module lang="scss">

</style>
