<script setup>
import {ref} from 'vue';

const id = ref('');

function parseInput(event) {
  const pre_id = event.target.value;
  id.value = pre_id.replace(/[^a-zA-Z]/g, '').toUpperCase().slice(0, 4);
}

</script>

<template>
<div :class="$style.cont">
  <div :class="$style.bmenu">
    <div :class="$style.text">
      Введите идентификатор метки с обратной стороны устройства.
    </div>
    <input :value="id" @change="parseInput" type="text" :class="$style.input">
    <button :class="$style.button" @click="parseInput">Подтвердить</button>
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
}

</style>