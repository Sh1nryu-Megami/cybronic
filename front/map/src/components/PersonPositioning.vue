<script setup>
import { ref, onMounted, watch } from 'vue';
import $ from 'jquery';
import {fetch_addr} from '/src/config';
import PersonPoint from '/src/components/images/PersonPoint.vue';

const devices = ref([]);
const devices_comp = ref([]);
const props = defineProps(['map']);
const layout = ref({
  width: 0,
  height: 0,
});

onMounted(() => {
  fetch(fetch_addr + 'api/getlayout')
  .then((resp) => resp.json())
  .then((data) => {
    layout.value.width = data.width
    layout.value.height = data.height
  });

  setTimeout(function get() {
    new Promise((res) => {
      fetch(fetch_addr + 'api/getall')
        .then((resp) => resp.json())
        .then((data) => {
          if (data[0] == undefined || data[0] == null) {
            return;
          }

          let arr = Object.entries(data[0]);
          devices.value = [];

          for (let i = 0; i < arr.length; i++) {
            devices.value.push({
              mac: arr[i][0],
              coords: JSON.parse(arr[i][1]),
              idx: i,
            });
          }
          res()
          setTimeout(get, 100)
        })
    })
  }, 100)
});

watch(() => ({devices: devices.value, updated: props.map.updated}), () => {
  let map = $("#map");
  const offset = map.offset();
  const map_width = map.width();
  const map_height = map.height();

  devices_comp.value = [];

  for (const {idx, mac, coords: {x, y}} of devices.value) {
    const x_rel = x / layout.value.width * map_width;
    const y_rel = y / layout.value.height * map_height;

    devices_comp.value.push({
      idx: idx,
      mac: mac,
      coords: {
        x: offset.left + x_rel,
        y: offset.top + y_rel,
      },
    });
  }
  // console.log(layout.value)
});

</script>

<template>
  <PersonPoint
    v-for="{idx, mac, coords: {x, y}} of devices_comp"
    :key="mac"
    :x="x"
    :y="y"
    :num="idx"
  />
</template>

<style module lang="scss">
@use '/src/colors';
</style>
