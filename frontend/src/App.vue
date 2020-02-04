<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <Customers :customers="customers" />
  </div>
</template>
<script>
import Customers from './components/Customers.vue'

export default {
  name: 'app',
  components: {
    Customers
  },
  data() {
    return {
      customers: [{
          'id': 1,
          'first_name': 'Regis',
          'last_name': 'Santos',
        },
        {
          'id': 2,
          'first_name': 'Ronaldo',
          'last_name': 'Silva',
        },
      ]
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