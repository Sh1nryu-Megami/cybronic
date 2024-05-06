<script setup>
import { ref, onMounted, watch } from 'vue'
import $ from 'jquery'

const devices = ref([])
const props = defineProps(['map'])

onMounted(() => {
  setTimeout(function get() {
    new Promise((res) => {
      fetch('http://192.168.0.12:8000/api/getall')
        .then((resp) => resp.json())
        .then((data) => {
          devices.value = Object.entries(data[0])

          for (let i = 0; i < devices.value.length; i++) {
            devices.value[i][1] = JSON.parse(devices.value[i][1])
          }
          res()
          setTimeout(get, 500)
        })
    })
  }, 500)
})

watch(() => ({devices: devices.value, updated: props.map.updated}), (shiftPoint) => {
  props.map.updated = false;
  for (let [mac, {x, y}] of devices.value) {
    let x_pos = x;
    let y_pos = y;
    let map_pos = $('#map').offset();
    $('#point' + mac).offset({left: map_pos.left + x_pos, top: map_pos.top + y_pos})
  }
  
})

</script>

<template>
  
  <div v-for="[mac, _] of devices" :key="mac" :class="$style.personPoint">
    <img :id="'point' + mac" src="/src/assets/person.svg" />
  </div>
</template>

<style module lang="scss">
@use '/src/colors';

.personPoint {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  touch-action: none;

  & > img {
    width: 2%;
    height: 1%;
    position: relative;
    top: 0;
    left: 0;
  }
}
</style>
