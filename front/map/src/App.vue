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

function set_init_false() {
  is_init.value = false;
}

function set_init_true() {
  is_init.value = true;
}

</script>

<template>
  <BackgroundMap :curPath="current_path" :init="is_init" />
  <BottomMenu :setPath="set_path" :setInitFalse="set_init_false" />
  <Getmac v-if="!is_init" :setInitTrue="set_init_true" />
  <!--<div id="log" style="color: white;">0</div> -->
</template>

<style module lang="scss">

</style>
