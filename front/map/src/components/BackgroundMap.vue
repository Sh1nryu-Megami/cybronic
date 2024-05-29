<script setup>
import { onMounted, onBeforeUnmount } from 'vue'
import { ref } from 'vue';
import {
  setStartPosWrapper,
  setEndPosWrapper,
  setCancelPosWrapper,
  setMovePosWrapper,
  onResizeWrapper,
} from '/src/handlers/bgMapHandler';
import PersonPositioning from '/src/components/PersonPositioning.vue';
import SideButtons from '/src/components/SideButtons.vue';
import { fetch_addr } from '/src/config.js';

const props = defineProps(['curPath', 'init']);

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
  updated: false,
});
const handlers = ref({
  start: setStartPosWrapper(position_data),
  end: setEndPosWrapper(position_data),
  cancel: setCancelPosWrapper(position_data),
  move: setMovePosWrapper(position_data),
  resize: onResizeWrapper(position_data),
});

onMounted(() => {
  img_ref.value.addEventListener('touchstart', handlers.value.start);
  document.addEventListener('touchend', handlers.value.end);
  img_ref.value.addEventListener('touchmove', handlers.value.move);
  document.addEventListener('touchcancel', handlers.value.cancel);
  document.addEventListener('resize', handlers.value.resize);
});

onBeforeUnmount(() => {
  img_ref.value.removeEventListener('touchstart', handlers.value.start);
  document.removeEventListener('touchend', handlers.value.end);
  img_ref.value.removeEventListener('touchmove', handlers.value.move);
  document.removeEventListener('touchcancel', handlers.value.cancel);
  document.removeEventListener('resize', handlers.value.resize);
});

// function zoom(newX, newY, newH, newW) {
//   position_data.value.map.h = newH;
//   position_data.value.map.w = newW;
//   position_data.value.map.x = newX;
//   position_data.value.map.y = newY;
// }

</script>

<template>
  <div :class="$style.bg_map" ref="img_ref">
    <img id="map" :src="fetch_addr + 'api/getview'" />
    <PersonPositioning :map="position_data" :init="props.init" :curPath="props.curPath" />
    <SideButtons />
  </div>
</template>

<style module lang="scss">
@use '/src/colors';

.bg_map {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  touch-action: none;

  &>img {
    height: 60%;
    position: relative;
    top: 10%;
    left: 0;
    transform: rotate(0deg);
  }
}
</style>
