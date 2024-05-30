<script setup>
import { onMounted, onBeforeUnmount } from 'vue'
import { ref, watch } from 'vue';
import {
  setStartPosWrapper,
  setEndPosWrapper,
  setCancelPosWrapper,
  setMovePosWrapper,
  onResizeWrapper,
} from '/src/handlers/bgMapHandler';
import PersonPositioning from '/src/components/PersonPositioning.vue';
import SideButtons from '/src/components/SideButtons.vue';
import PersonPoint from '/src/components/images/PersonPoint.vue';
import { fetch_addr } from '/src/config.js';
import { getTouchMove, getTouchStart } from '/src/handlers/moveHandlers.js';
import $ from 'jquery';

const props = defineProps(['curPath', 'init']);

const img_ref = ref();
const move_ref = ref();
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
const layout = ref({
  width: 0,
  height: 0,
});
const moveData = ref({
  x: 0,
  y: 0,
});
const moveDataReal = ref({
  x: 0,
  y: 0,
});
const realCoords = ref({
  x: 0,
  y: 0,
});
const realCoordsPrj = ref({
  x: 0,
  y: 0,
});
const handlers = ref({
  start: setStartPosWrapper(position_data),
  end: setEndPosWrapper(position_data),
  cancel: setCancelPosWrapper(position_data),
  move: setMovePosWrapper(position_data),
  resize: onResizeWrapper(position_data),
  moveMove: getTouchMove(moveData),
  moveStart: getTouchStart(moveData),
});
const halls = ref({});

onMounted(() => {
  fetch(fetch_addr + 'api/gethalls').then(res => res.json()).then(res => {
    halls.value = res;
  });

  fetch(fetch_addr + 'api/getlayout')
  .then((resp) => resp.json())
  .then((data) => {
    layout.value.width = data.width
    layout.value.height = data.height
  });

  img_ref.value.addEventListener('touchstart', handlers.value.start);
  document.addEventListener('touchend', handlers.value.end);
  img_ref.value.addEventListener('touchmove', handlers.value.move);
  document.addEventListener('touchcancel', handlers.value.cancel);
  document.addEventListener('resize', handlers.value.resize);
  move_ref.value.addEventListener('touchmove', handlers.value.moveMove);
  move_ref.value.addEventListener('touchstart', handlers.value.moveStart);

  setInterval(() => {
    const mac = localStorage.getItem('mac');
    fetch(fetch_addr + 'api/getvertex/' + mac + '/' + realCoords.value.x + '/' + realCoords.value.y).catch(e => console.log(e));
  }, 500);
});

onBeforeUnmount(() => {
  img_ref.value.removeEventListener('touchstart', handlers.value.start);
  document.removeEventListener('touchend', handlers.value.end);
  img_ref.value.removeEventListener('touchmove', handlers.value.move);
  document.removeEventListener('touchcancel', handlers.value.cancel);
  document.removeEventListener('resize', handlers.value.resize);
  move_ref.value.removeEventListener('touchmove', handlers.value.moveMove);
  move_ref.value.removeEventListener('touchstart', handlers.value.moveStart);
});

function setUpdated() {
  position_data.value.updated = !position_data.value.updated;
}

watch(() => JSON.stringify(moveData.value), () => {
  console.log('data move')
  let map = $('#map');
  const mapOffset = map.offset();
  const mapWidth = map.width();
  const ratio = mapWidth / layout.value.width;
  const x = (moveData.value.x - mapOffset.left) / ratio;
  const y = (moveData.value.y - mapOffset.top) / ratio;
  moveDataReal.value.x = x;
  moveDataReal.value.y = y;

  let min_dist = 100000000;
  let real_x = 0;
  let real_y = 0;

  for (let hall of Object.values(halls.value)) {
    if (hall.id.endsWith('_hor') && hall.x <= x && x <= hall.x + hall.width) {
      if (Math.abs(y - hall.baseline) < min_dist) {
        // console.log('Hor')
        min_dist = Math.abs(y - hall.baseline);
        real_x = x;
        real_y = hall.baseline;
      }
    } 
    else if (hall.id.endsWith('_vert') && hall.y <= y && y <= hall.y + hall.height) {
      if (Math.abs(x - hall.baseline) < min_dist) {
        // console.log('Vert')
        min_dist = Math.abs(x - hall.baseline);
        real_x = hall.baseline;
        real_y = y;
      }
    }
  }

  realCoords.value = {
    x: real_x,
    y: real_y,
  };

  realCoordsPrj.value = {
    x: real_x * ratio + mapOffset.left,
    y: real_y * ratio + mapOffset.top,
  };
});

watch(() => position_data.value.updated, () => {
  console.log('data updated')
  let map = $("#map");
  const offset = map.offset();
  const map_width = map.width();
  const map_height = map.height();
  
  let x_rel = realCoords.value.x / layout.value.width * map_width;
  let y_rel = realCoords.value.y / layout.value.height * map_height;

  realCoordsPrj.value.x = offset.left + x_rel;
  realCoordsPrj.value.y = offset.top + y_rel; 

  x_rel = moveDataReal.value.x / layout.value.width * map_width;
  y_rel = moveDataReal.value.y / layout.value.height * map_height;

  moveData.value.x = offset.left + x_rel;
  moveData.value.y = offset.top + y_rel;
});

</script>

<template>
  <div :class="$style.bg_map" ref="img_ref">
    <img id="map" :src="fetch_addr + 'api/getview'" />
    <PersonPositioning :map="position_data" :init="props.init" :curPath="props.curPath" />
    <SideButtons :update="setUpdated" />
    <PersonPoint num="2" :x="realCoordsPrj.x" :y="realCoordsPrj.y" />
    <div :class="[$style.move, 'move']" ref="move_ref" :style="{left: moveData.x + 'px', top: moveData.y + 'px'}">
      <PersonPoint num="1" x="10" y="10" />
    </div>
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

.move {
  position: absolute;
  $size: 30px;
  width: $size;
  height: $size;
  top: 50%;
  left: 50%;
  touch-action: none;
}
</style>
