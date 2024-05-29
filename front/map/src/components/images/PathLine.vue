<script setup>

const props = defineProps(['x1', 'y1', 'x2', 'y2']);

</script>

<template>
<div
  :class="$style.line"
  :style="{left: props.x1, top: props.y1, width: Math.abs(props.x2 - props.x1), height: Math.abs(props.y2 - props.y1)}"
>
</div>
</template>

<style module lang='scss'>
@use '/src/colors';

.line {
  background-color: #C57BFF;
  position: absolute;
}

</style>