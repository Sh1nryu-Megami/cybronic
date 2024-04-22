<script setup>
import { ref, onMounted } from "vue";

const devices = ref([]);

onMounted(() => {
  setTimeout(function get() {
    new Promise((res) => {
      fetch("http://192.168.1.149/api/getall")
      .then((resp) => resp.json())
      .then((data) => {
        devices.value = Object.entries(data[0]).slice(1);

        for (let i = 0; i < devices.value.length; i++) {
          devices.value[i][1] = JSON.parse(devices.value[i][1]);
        }

        res();
        setTimeout(get, 500);
       })
    })
  }, 500);
});

</script>

<template>
  <div class="title">
    <h1>Координаты BLE меток и смартфонов в комплексе Olvery №12</h1>
  </div>

  <table class="table">
    <thead>
      <tr>
        <th scope="col">Название</th>
        <th scope="col"><img src="/src/assets/blue_mark.svg" />X координата</th>
        <th scope="col"><img src="/src/assets/red_mark.svg" />Y координата</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="[mac, {x, y}] of devices" :key="mac">
        <td>
          {{ mac }}
        </td>
        <td>
          {{ x }}
        </td>
        <td>
          {{ y }}
        </td>
      </tr>
    </tbody>
  </table>
</template>

<style scoped>
.title {
  text-align: left;
  font-family: 'Lucida Sans Unicode';
  border-bottom: 2px solid #e9e9e7;
  margin-bottom: 2rem;
}
</style>
