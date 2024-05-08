<script setup>
defineProps({
  type: {
    type: String,
    default: 'text'
  }
});
</script>

<template>
<div class="$styles.cont">
  <input
    class="$style.input"
    :type="type"
  />
</div>
</template>

<style module lang='scss'>
@use '/src/colors';

.cont {
  width: 100%;
}

.input {
  width: 100%;
  padding: 5px;
  box-sizing: border-box;
  border-radius: 20px;
  
}

</style>