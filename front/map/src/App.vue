<script setup>
<<<<<<< HEAD
  function dropDown() {
    document.getElementById("dropDownList")?.classList.toggle("show");
  }
</script>

<template>
  <header>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </header>
  <body>
    <component :is="'script'" src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></component>
    
    <div class="mb-3">
      <input onclick="dropDown()" type="text" class="form-control" id="formGroupExampleInput" placeholder="Поиск">
      <div id="dropDownList" class="list-group">
        <a href="#" class="list-group-item list-group-item-action">Аудитория 1</a>
        <a href="#" class="list-group-item list-group-item-action">Аудитория 2</a>
        <a href="#" class="list-group-item list-group-item-action">Аудитория 3</a>
        <a href="#" class="list-group-item list-group-item-action">Аудитория 4</a>
        <a href="#" class="list-group-item list-group-item-action">Аудитория 5</a>
        <a href="#" class="list-group-item list-group-item-action">Аудитория 97</a>
      </div>
    </div>

    <div class="plus-minus-loc-buttons">
      <button type="button" class="btn btn-primary">+</button>
      <button type="button" class="btn btn-primary">-</button>
      <button type="button" class="btn btn-primary"><img src="/src/assets/location-mark.svg"></button>
    </div>

  </body>

  
</template>

<style scoped>

header {
  line-height: 1.5;
  display: flex;
}

ul {
  display: flex
}

.list-group:hover {
  display: flex
}

.list-group {
  position: absolute;
}
=======
import BottomMenu from './components/BottomMenu.vue'
import BackgroundMap from './components/BackgroundMap.vue'
</script>

<template>
  <BackgroundMap />
  <BottomMenu />
  <!--<div id="log" style="color: white;">0</div> -->
</template>

<style module lang="scss">

>>>>>>> 5937f6491c697067517b997933a718312b96d743
</style>
