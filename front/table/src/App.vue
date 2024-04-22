<script>
export default {
  data() {
    return {
      devices: [],
      device_name: '',
      x_coord: '',
      y_coord: ''
    }
  },
  methods: {
    addDevice() {
      this.devices.push({
        device_name: this.device_name,
        x_coord: this.x_coord,
        y_coord: this.y_coord
      })
    }
  }
}
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
      <tr v-for="(device, index) in devices" :key="index">
        <td>
          {{ device.device_name }}
        </td>
        <td>
          {{ device.x_coord }}
        </td>
        <td>
          {{ device.y_coord }}
        </td>
      </tr>
    </tbody>
  </table>

  <input type="text" v-model="device_name" />
  <input type="text" v-model="x_coord" />
  <input type="text" v-model="y_coord" />
  <button @click="addDevice()">add</button>
</template>

<style scoped>
.title {
  text-align: left;
  font-family: 'Lucida Sans Unicode';
  border-bottom: 2px solid #e9e9e7;
  margin-bottom: 2rem;
}
</style>
