<script setup>
import BottomMenu from './components/BottomMenu.vue'
import BackgroundMap from './components/BackgroundMap.vue'
import Getmac from './components/GetMac.vue'
import { onMounted, ref } from 'vue';

const is_init = ref(false);
const current_path = ref(null);

onMounted(() => {
  if (localStorage.getItem('mac') !== null) {
    is_init.value = true;
  }
});

function set_path(path) {
  current_path.value = path;
  return path;
}

</script>

<template>
  <BackgroundMap :curPath="current_path" :init="is_init" />
  <BottomMenu :setPath="set_path" />
  <Getmac v-if="!is_init" />
  <!--<div id="log" style="color: white;">0</div> -->
</template>

<style module lang="scss">

</style>
