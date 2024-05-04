<script setup>
import { onMounted, onUnmounted } from 'vue'
import { ref } from 'vue'

const img_ref = ref()
const position_data = ref({
  touched: false,
  map: {
    x: 0,
    y: 0,
    w: 0,
    h: 0
  },
  startFingers: [],
  endFingers: [],
  img_ref: img_ref
})

onMounted(() => {
  img_ref.value.addEventListener('touchstart', setStartPosWrapper(position_data))
  img_ref.value.addEventListener('touchend', setEndPosWrapper(position_data))
  img_ref.value.addEventListener('touchmove', setMovePosWrapper(position_data))
  img_ref.value.addEventListener('touchcancel', setCancelPosWrapper(position_data))
})

// onUnmounted(() => {
//   img_ref.value.removeEventListener('touchstart')
// })
</script>

<template>
  <div class="$style.bg_map">
    <img src="../assets/map_tmp.svg" ref="img_ref" />
  </div>
</template>

<style module lang="scss">
@use '/src/colors';
.bg_map {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  & > img {
    width: 100%;
    height: 100%;
  }
}
</style>
