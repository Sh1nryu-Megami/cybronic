<script setup>
import {colors} from "/src/config/personPointColors";

const props = defineProps(['num', 'x', 'y']);

</script>

<template>
<svg
  width="32"
  height="32"
  viewBox="0 0 32 32"
  fill="none"
  xmlns="http://www.w3.org/2000/svg"
  :class="[$style.cont, 'personPoint']"
  :style="{left: props.x, top: props.y}"
>
  <circle cx="16" cy="16" r="16" fill="#FFF9EA"/>
  <circle cx="16" cy="16" r="9" :fill="colors[props.num % colors.length]"/>
</svg>
</template>

<style module lang='scss'>
@use '/src/colors';

.cont {
  position: absolute;
  
  $size: 10px;
  width: $size;
  height: $size;
}

</style>