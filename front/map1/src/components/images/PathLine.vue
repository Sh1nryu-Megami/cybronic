<script setup>
import {computed} from "vue";
const props = defineProps(['x1', 'y1', 'x2', 'y2']);

const tight = 3;

const style = computed(() => {
  let _top = 0, _left = 0, _width = 0, _height = 0;

  if (Math.abs(props.x1 - props.x2) <= tight * 2) {
    _left = props.x1 - tight;
    _top = Math.min(props.y1, props.y2) - tight;
    _width = tight * 2;
    _height = Math.abs(props.y2 - props.y1) + 2 * tight;
  } else {
    _left = Math.min(props.x1, props.x2) - tight;
    _top = props.y1 - tight;
    _width = Math.abs(props.x2 - props.x1) + 2 * tight;
    _height = tight * 2;
  }
  
  return {
    top: _top + 'px',
    left: _left + 'px',
    width: _width + 'px',
    height: _height + 'px',
  };
});


</script>

<template>
<div
  :class="$style.line"
  :style="style"
>
</div>
</template>

<style module lang='scss'>
@use '/src/colors';

.line {
  background-color: colors.$path;
  position: absolute;
  border-radius: 2px;
  display: block;
  // border: solid 2px #C57BFF;
  animation: show 1s ease-in-out 1;
  // opacity: 1;
  // content: '';
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