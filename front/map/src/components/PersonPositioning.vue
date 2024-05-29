<script setup>
import { ref, onMounted, watch } from 'vue';
import $ from 'jquery';
import {fetch_addr} from '/src/config';
import PersonPoint from '/src/components/images/PersonPoint.vue';

const props = defineProps(['map', 'init', 'curPath']);

const device = ref({
  x: 0,
  y: 0,
});

const device_comp = ref({
  x: 0,
  y: 0,
});

// const path = ref([]);

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

  // console.log('aa')
}

onMounted(() => {
  fetch(fetch_addr + 'api/getlayout')
  .then((resp) => resp.json())
  .then((data) => {
    layout.value.width = data.width
    layout.value.height = data.height
  });

  interval_id.value = setInterval(getPos, 100);
});

watch(() => props.init, () => {
  clearInterval(interval_id.value);
  interval_id.value = setInterval(getPos, 100);
});

watch(() => ({device: device.value, updated: props.map.updated}), () => {
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

  console.log(device.value.x, device.value.y);
  console.log(device_comp.value.x, device_comp.value.y);
});

</script>

<template>
  <PersonPoint
    :x="device_comp.x"
    :y="device_comp.y"
    :num="0"
  />
</template>

<style module lang="scss">
@use '/src/colors';
</style>
