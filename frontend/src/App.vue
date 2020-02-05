<template>
  <div id="app">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
    <img alt="Vue logo" src="./assets/logo.png">
    <Customers/>
  </div>
</template>

<script>
import Customers from './components/Customers.vue'

export default {
  name: 'app',
  components: {
    Customers
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