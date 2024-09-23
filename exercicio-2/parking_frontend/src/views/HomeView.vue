<template>
    <div>
      <h1>Operation</h1>
      
      <div>
        <label>Placa</label>
        <input type="text" v-model="licensePlate" placeholder="Enter License Plate" />
        
        <label>Valor a cobrar</label>
        <input type="text" v-model="chargeValue" disabled />
        
        <button @click="checkIn">Entrada</button>
        <button :disabled="!canCheckOut" @click="checkOut">Saída</button>
      </div>
  
      <h2>Vehicles in the Patio</h2>
      <table>
        <thead>
          <tr>
            <th>Data de Entrada</th>
            <th>Placa</th>
            <th>Cartão</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="vehicle in vehicles" :key="vehicle.id">
            <td>{{ vehicle.entry_date }}</td>
            <td>{{ vehicle.plate }}</td>
            <td>{{ vehicle.card }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import api from '@/services/api';
  
  export default {
    data() {
      return {
        licensePlate: '',
        chargeValue: '',
        vehicles: [],
        canCheckOut: false,
      };
    },
    created() {
      this.fetchVehicles();
    },
    methods: {
      fetchVehicles() {
        api.get('/parkmovement')
          .then(response => {
            this.vehicles = response.data;
          })
          .catch(error => {
            console.error('Failed to load vehicles:', error);
          });
      },
      checkIn() {
        api.post('/parkmovement', { plate: this.licensePlate })
          .then(() => {
            this.fetchVehicles(); // Refresh the vehicle list
          })
          .catch(error => {
            console.error('Failed to check in:', error);
          });
      },
      checkOut() {
        // Implement check-out logic with API here
        // Set `canCheckOut` to false after successful check-out
      },
    }
  };
  </script>
  