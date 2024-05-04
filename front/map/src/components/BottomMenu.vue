<script setup>

</script>

<template>
  <div class="$style.cont">
    <div class="$style.input"></div>
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

</style>