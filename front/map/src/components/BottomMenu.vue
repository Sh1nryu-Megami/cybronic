<script setup>

import { ref } from "vue"
import { onMounted } from 'vue'
import { fetch_addr } from '/src/config.js';
import SearchSvg from '/src/assets/search.svg';
import ClearSvg from '/src/assets/clear_button.svg';
import SettingsSvg from '/src/assets/settings.svg';
import ArrowSvg from '/src/assets/arrow.svg';

const props = defineProps(['setPath', 'setInitFalse']);

const input_text = ref('');
const rooms = ref([]);
const matchedRooms = ref([]);
const search_focus = ref(false);
const cont_ref = ref(null);
const current_path = ref(null);


onMounted(() => {
  fetch(fetch_addr + 'api/getallrooms')
    .then((resp) => resp.json())
    .then((data) => {
      rooms.value = Object.keys(data);
      matchedRooms.value = Object.keys(data);
    });
})

function agregateRooms(event) {
  let escaped = event.target.value.replace(/\[|\]|\\|\^|\$|\.|\?|\*|\+|\(|\)/gi, '\\$&');
  let search_pattern = new RegExp(escaped.split(' ').reduce((acc, cur) => acc + cur + '.*', '.*'), 'i');
  matchedRooms.value = rooms.value.filter((room) => room.match(search_pattern));
  matchedRooms.value.sort();
  // matchedRooms.value = matchedRooms.value.map((room) => room.slice(event.target.value.length));

  input_text.value = event.target.value;
}

function inputFocus() {
  search_focus.value = true;
}

function clearInput() {
  current_path.value = props.setPath(null);
  input_text.value = '';
  matchedRooms.value = rooms.value;
}

function showPath(event) {
  current_path.value = props.setPath(event.currentTarget.getAttribute('value'));
}

function openSettings() {
  props.setInitFalse();
}

</script>

<template>
  <div :class="[$style.cont, search_focus && $style.contUp]" ref="cont_ref">
    <div :class="$style.topLine" :style="{display: input_text !== '' || search_focus ? 'block' : 'none'}">
      <div></div>
    </div>
    <div :class="$style.input">
      <img :src="SearchSvg" alt="search" />
      <div>
        <input
          v-if="current_path === null"
          type="text"
          @input="agregateRooms"
          :value="input_text"
          placeholder="Поиск аудиторий"
          @focusin="inputFocus"
          @focusout="search_focus = false"
        />
        <div
          v-else
          :class="$style.path"
        >
          <div>
            Путь до
          </div>
          <img :src="ArrowSvg" alt="arrow" />
          <div>
            {{ current_path }}
          </div>
        </div>
      </div>
      <button v-if="!(input_text !== '' || current_path !== null)" :class="$style.settings" @click="openSettings">
        <img :src="SettingsSvg" alt="settings" />
      </button>
      <button v-else :class="$style.clear_button" @click="clearInput">
        <img :src="ClearSvg" alt="claer input" />
      </button>
    </div>
    <div :class="[$style.resualts, search_focus ? $style.resualtsShow : $style.resualtsHide]">
      <div :class="$style.searchResualt" v-for="room of matchedRooms" :key="room" @click="showPath" :value="room">
        {{ room }}
      </div>
    </div>
  </div>
</template>

<style module lang='scss'>
@use '/src/colors';

.cont {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 180px;
  border-top-left-radius: 50px;
  border-top-right-radius: 50px;
  background-color: colors.$menu_bg;
  box-sizing: border-box;
  padding: 30px 20px 50px 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: all 0.5s ease-in-out;
}

.contUp {
  height: 80%;
}

.topLine {
  position: absolute;
  top: -5px;
  left: 0;
  width: 100%;
  height: 35px;

  &>div {
    $width: 40px;
    position: absolute;
    top: 18px;
    left: calc(50% - $width / 2);
    width: $width;
    height: 5px;
    border-radius: 5px;
    background-color: colors.$line_color;
  }
}

.input {
  width: 100%;
  margin-bottom: 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;

  &>img {
    width: 25px;
    margin-right: 10px;
  }

  &>div {
    flex-grow: 1;

    &>input {
      width: 100%;
      border: none;
      border-radius: 10px;
      background-color: colors.$input_bg;
      font-size: 14px;
      padding: 10px;
      box-sizing: border-box;
      font-size: 20px;
      font-weight: bold;
      outline: none;
      color: colors.$outer_circle;
    }
  }
}

.path {
  width: 100%;
  border-radius: 10px;
  background-color: colors.$input_bg;
  font-size: 14px;
  padding: 10px;
  box-sizing: border-box;
  font-size: 20px;
  font-weight: bold;
  color: colors.$outer_circle;
  display: flex;
  align-items: center;

  &>img {
    height: 14px;
  }

  &>* {
    margin-right: 10px;
  }
}

.settings {
  width: 35px;
  background-color: #00000000;
  outline: none;
  border: none;
  margin-left: 10px;

  &>img {
    width: 100%;
  }
}

.clear_button {
  width: 25px;
  border: none;
  outline: none;
  background-color: #00000000;
  margin-left: 15px;
  margin-right: 5px;

  &>img {
    width: 100%;
  }
}

.resualts {
  width: 100%;
  padding-left: 45px;
  transition: all 0.5s ease-in-out;
  flex-grow: 1;
  overflow-y: scroll;
  overflow-x: hidden;
}

.resualtsShow {
  opacity: 1;
}

.resualtsHide {
  opacity: 0;
}

.searchResualt {
  margin-bottom: 10px;
  color: colors.$outer_circle;
  font-size: 18px;
  font-weight: bold;
}

</style>