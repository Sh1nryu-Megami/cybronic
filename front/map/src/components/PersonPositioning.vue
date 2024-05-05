<script setup>
import { ref, onMounted, watch } from 'vue'
import $ from 'jquery'

const devices = ref([])
const img_ref = ref()

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

watch(devices, (shiftPoint) => {
  let position = devices.value[0][1];
  let x_pos = position.x;
  let y_pos = position.y;
  $('#point').offset({ left: x_pos, top: y_pos });
})
</script>

<template>
  <div :class="$style.personPoint" ref="img_ref">
    <img id="point" src="/src/assets/person.svg" />
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
    top: 50px;
    left: 5px;
  }
}
</style>
