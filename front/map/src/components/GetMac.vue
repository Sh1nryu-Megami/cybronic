<script setup>
import {ref} from 'vue';
import {fetch_addr} from '/src/config.js';

const id = ref('');
const error = ref(false);
const closed = ref(false);

function parseInput(event) {
  const pre_id = event.target.value;
  id.value = pre_id.replace(/[^a-zA-Z]/g, '').toUpperCase().slice(0, 4) || '';
  event.target.value = id.value;
}

async function checkID() {
  const resp = await fetch(fetch_addr + 'api/getmacbyaaaa/' + id.value);
  const data = await resp.json();
  
  if (data.error !== undefined) {
    error.value = true;
  } else {
    error.value = false;
  }

  if (data.answer !== undefined) {
    localStorage.setItem('mac', data.answer);
    closed.value = true;
  }
}

</script>

<template>
<div :class="[$style.cont, closed ? $style.contClosed : $style.contOpen]">
  <div :class="$style.bmenu">
    <div :class="$style.text">
      Введите идентификатор метки с обратной стороны устройства.
    </div>
    <div :class="$style.inputWrapper">
      <input 
        :value="id"
        @input="parseInput"
        type="text"
        :class="$style.input"
        placeholder="????"
        maxlength="4"
      />
      <div :class="$style.errorText" :style="{opacity: error ? 1 : 0}">
        Такого идентификатора нет
      </div>
    </div>
    <button
      :class="[$style.button, id.length == 4 ? $style.buttonActive : $style.buttonDisabled]"
      @click="checkID"
    >
      Подтвердить
    </button>
  </div>
</div>
</template>

<style module lang='scss'>
@use '/src/colors';

.cont {
  width: 100vw;
  height: 100vh;
  position: fixed;
  left: 0;
  touch-action: none;
  transition: top 0.5s ease-out;
}

.contOpen {
  top: 0;
}

.contClosed {
  top: 100vh;
}

.bmenu {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 80%;
  border-top-left-radius: 50px;
  border-top-right-radius: 50px;
  background-color: colors.$menu_bg;
  box-sizing: border-box;
  padding: 50px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.text {
  font-size: 15px;
  font-weight: 500;
  color: colors.$outer_circle;
  margin-bottom: 40px;
  text-align: center;
}

.errorText {
  font-size: 15px;
  font-weight: 500;
  color: colors.$error;
  text-align: center;
  transition: all 0.5s ease-in-out;
}

.inputWrapper {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 30px;
}

.input {
  $font-size: 50px;
  width: 4 * $font-size;
  outline: none;
  border: none;
  box-sizing: border-box;
  padding: 20px;
  border-radius: 15px;
  background-color: colors.$input_bg;
  text-align: center;
  font-size: $font-size;
  color: colors.$outer_circle;
  margin-bottom: 15px;
}

.button {
  box-sizing: border-box;
  padding: 15px 30px;
  border-radius: 10px;
  font-size: 20px;
  color: colors.$outer_circle;
  outline: none;
  border: none;
  font-weight: bold;
  transition: all 0.7s;
}

.buttonActive {
  background-color: colors.$active_button;
}

.buttonDisabled {
  background-color: colors.$text;
}

</style>