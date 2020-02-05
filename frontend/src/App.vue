<template>
  <div id="app">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
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
      customers: [],
      // first_name: '',
      // last_name: '',
    }
  },
  created() {
    axios.get(endpoint + '/api/customers/')
      .then(response => {
        this.customers = response.data.data
      })
  },
  methods: {
    saveCustomers() {
      let bodyFormData = new FormData();
      // let config = { headers: {'Content-Type': 'multipart/form-data'} }
      bodyFormData.append('first_name', this.first_name);
      bodyFormData.append('last_name', this.last_name);

      axios.post(endpoint + '/api/customers/add/')
        .then(response => {
          this.customers = response.data.data
        })
    }
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