<script setup>
import { ref, onMounted, onBeforeUnmount, watch } from 'vue';
import $ from 'jquery';
import {fetch_addr} from '/src/config';
import PersonPoint from '/src/components/images/PersonPoint.vue';
import PathLine from '/src/components/images/PathLine.vue';

const props = defineProps(['map', 'init', 'curPath']);

const device = ref({
  x: 0,
  y: 0,
});

const device_comp = ref({
  x: 0,
  y: 0,
});

const path = ref([]);
const path_comp = ref([]);

const layout = ref({
  width: 0,
  height: 0,
});
const interval_id = ref(0);

async function getPos() {
  let mac = localStorage.getItem('mac');

  let data = await fetch(fetch_addr + 'api/getcoordbymac/' + mac);
  data = await data.json();
  data = JSON.parse(data);

  if (data.x === undefined || data.y === undefined) {
    return;
  }


  device.value.x = data.x;
  device.value.y = data.y;
}

onMounted(() => {
  fetch(fetch_addr + 'api/getlayout')
  .then((resp) => resp.json())
  .then((data) => {
    layout.value.width = data.width
    layout.value.height = data.height
  });

  interval_id.value = setInterval(getPos, 200);
});

onBeforeUnmount(() => {
  clearInterval(interval_id.value);
});

watch(() => props.init, () => {
  clearInterval(interval_id.value);
  interval_id.value = setInterval(getPos, 200);
});

watch(() => JSON.stringify(device.value) + JSON.stringify(props.map.updated), () => {
  // console.log('aa')
  let map = $("#map");
  let personPoint = $(".personPoint");
  const offset = map.offset();
  const map_width = map.width();
  const map_height = map.height();
  let pointOffsetX = 0;
  let pointOffsetY = 0;
  
  if (personPoint.length != 0) {
    const width = personPoint.width();
    const height = personPoint.height();

    pointOffsetX = width / 2;
    pointOffsetY = height / 2;
  }
  
  const x_rel = device.value.x / layout.value.width * map_width;
  const y_rel = device.value.y / layout.value.height * map_height;

  device_comp.value.x = offset.left + x_rel - pointOffsetX;
  device_comp.value.y = offset.top + y_rel - pointOffsetY;
});

watch(() => props.curPath, async () => {
  if (props.curPath === null) {
    path.value = [];
    // console.log('path cleared');
  } else {
    const mac = localStorage.getItem('mac');
    let data = await fetch(fetch_addr + 'api/getpath/' + mac + '/' + props.curPath);
    data = await data.json();
    // console.log('path fetched');

    if (data === 'error') {
      return;
    } else {
      console.log(data)
      path.value = data;
    }
  }
});

watch(() => JSON.stringify(path.value) + JSON.stringify(props.map.updated), () => {
  let map = $("#map");
  const offset = map.offset();
  const map_width = map.width();
  const map_height = map.height();

  path_comp.value = [];

  for (let i = 1; i < path.value.length; i++) {
    let x_1_rel = path.value[i - 1].x / layout.value.width * map_width;
    let y_1_rel = path.value[i - 1].y / layout.value.height * map_height;
    let x_2_rel = path.value[i].x / layout.value.width * map_width;
    let y_2_rel = path.value[i].y / layout.value.height * map_height;

    path_comp.value.push({
      x1: offset.left + x_1_rel,
      y1: offset.top + y_1_rel,
      x2: offset.left + x_2_rel,
      y2: offset.top + y_2_rel,
      id: String(path.value[i - 1].x) + String(path.value[i].x) + String(path.value[i - 1].y) + String(path.value[i].y)
    });
  }
});

</script>

<template>
  <PersonPoint
    :x="device_comp.x"
    :y="device_comp.y"
    :num="0"
  />
  <PathLine
    v-for="{x1, x2, y1, y2, id} of path_comp"
    :key="id"
    :x1="x1"
    :x2="x2"
    :y1="y1"
    :y2="y2"
  />
  <div
    v-if="path_comp.length !== 0"
    :class="$style.circle"
    :style="{
      top: path_comp[path_comp.length - 1].y2 - 8 + 'px',
      left: path_comp[path_comp.length - 1].x2 - 8 + 'px'
    }"
  ></div>
</template>

<style module lang="scss">
@use '/src/colors';

.circle {
  position: absolute;
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background-color: colors.$path;
  animation: show 1s ease-in-out 1;
}

@keyframes show {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

</style>
