<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <Customers :customers="customers" />
  </div>
</template>
<script>
import Customers from './components/Customers.vue'
import axios from 'axios'

const endpoint = 'http://localhost:8000'

export default {
  name: 'app',
  components: {
    Customers
  },
  data() {
    return {
      customers: []
    }
  },
  created() {
    axios.get(endpoint + '/api/customers/')
      .then(response => {
        this.customers = response.data.data
      })
  }
}
</script>
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>