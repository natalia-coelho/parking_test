<template>
  <div>
    <h1>Cadastro de Veículos</h1>
    <form @submit.prevent="saveVehicle" class="vehicle-form">
      <label>Placa</label>
      <input type="text" v-model="vehicle.plate" placeholder="Enter License Plate" required />

      <label>Modelo</label>
      <input type="text" v-model="vehicle.model" placeholder="Enter Model" required />

      <button type="submit">Salvar</button>
    </form>

    <h2>Veículos Cadastrados</h2>
    <ul class="vehicle-list">
      <li v-for="vehicle in vehicles" :key="vehicle.id">
        {{ vehicle.plate }} - {{ vehicle.model }}
      </li>
    </ul>
  </div>
</template>

<script>
import api from '@/services/api';

export default {
  data() {
    return {
      vehicle: {
        plate: '',
        model: ''
      },
      vehicles: []
    };
  },
  created() {
    this.fetchVehicles();
  },
  methods: {
    fetchVehicles() {
      api.get('/vehicle')
        .then(response => {
          this.vehicles = response.data;
        })
        .catch(error => {
          console.error('Failed to load vehicles:', error);
        });
    },
    saveVehicle() {
      api.post('/vehicle', this.vehicle)
        .then(() => {
          this.fetchVehicles(); // Refresh the vehicle list
          this.vehicle.plate = '';
          this.vehicle.model = '';
        })
        .catch(error => {
          console.error('Failed to save vehicle:', error);
        });
    },
  }
};
</script>

<style scoped>
.vehicle-form
{
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.vehicle-form input
{
  padding: 0.75rem;
  border: 1px solid var(--secondary-color);
  border-radius: 8px;
}

.vehicle-form button
{
  align-self: flex-start;
}

.vehicle-list
{
  list-style-type: none;
  padding: 0;
}

.vehicle-list li
{
  background-color: var(--white);
  padding: 1rem;
  margin-bottom: 1rem;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}
</style>
