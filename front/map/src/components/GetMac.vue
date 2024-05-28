<script setup>
import {ref} from 'vue';

const id = ref('');

function parseInput(event) {
  const pre_id = event.target.value;
  id.value = pre_id.replace(/[^a-zA-Z]/g, '').toUpperCase().slice(0, 4) || '';
  event.target.value = id.value;
}

</script>

<template>
<div :class="$style.cont">
  <div :class="$style.bmenu">
    <div :class="$style.text">
      Введите идентификатор метки с обратной стороны устройства.
    </div>
    <input 
      :value="id"
      @input="parseInput"
      type="text"
      :class="$style.input"
      placeholder="????"
      maxlength="4"
    />
    <div :class="$style.errorText">
      Такого идентификатора нет
    </div>
    <button
      :class="[$style.button, id.length == 4 ? $style.buttonActive : $style.buttonDisabled]"
      @click="parseInput"
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
  top: 0;
  left: 0;
  touch-action: none;
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
  margin-bottom: 40px;
  text-align: center;
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
  margin-bottom: 40px;
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