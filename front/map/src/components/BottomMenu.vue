<script setup>

import { ref } from "vue"
import { onMounted } from 'vue'
import { fetch_addr } from '/src/config.js';

const input_text = ref('');
const rooms = ref([]);
const matchedRooms = ref([]);


onMounted(() => {
  fetch(fetch_addr + 'api/getallrooms')
    .then((resp) => resp.json())
    .then((data) => {
      rooms.value = Object.keys(data);
    });
})

function agregateRooms(event) {
  let regValue = new RegExp('^' + event.target.value);
  matchedRooms.value = rooms.value.filter((room) => room.match(regValue));
  matchedRooms.value.sort();
  matchedRooms.value = matchedRooms.value.map((room) => room.slice(event.target.value.length));
  input_text.value = event.target.value;
}

function clearInput(event) {
  input_text.value = '';
  matchedRooms.value = rooms.value;
}

function showPath(event) {
  input_text.value = "Путь до -> " + event.currentTarget.getAttribute('value');
  matchedRooms.value = [];
  // TODO: сделать отображения маршрута
}

</script>

<template>
  <div :class="$style.cont">
    <div :class="$style.input">
      <input type="text" @input="agregateRooms" :value="input_text" />
      <button :class="$style.clear_button" @click="clearInput"></button>
      <div :class="$style.search_resualt" v-for="room of matchedRooms" @click="showPath" :value="input_text + room">
        <div :class="$style.matched"> {{ input_text }} </div>
        <div :class="$style.unmatched"> {{ room }} </div>
      </div>

    </div>

  </div>
</template>

<style module lang='scss'>
@use '/src/colors';

.cont {
  background-color: colors.$menu_bg;
  width: 100%;
  padding: 20px;
  box-sizing: border-box;
  position: absolute;
  bottom: 0;
  left: 0;
}

.input {
  width: 100%;
  margin-bottom: 40px;
}

.clear_button {
  height: 14px;
  width: 14px;
  border: none;
  background-color: colors.$menu_bg;
  margin-left: 0.3%;
  background-image: url("../assets/cross-square.svg");
  background-size: cover;
}

.search_resualt {
  display: flex;
  font-size: 10px;
}

.matched {
  color: white;
}

.unmatched {
  color: gray;
}
</style>