<template>
  <div>
    <h1>Clientes</h1>
    <table class="table">
      <thead>
        <tr>
          <th>Nome</th>
          <th>Sobrenome</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in customers" :key="item.id">
          <td>{{ item.first_name }}</td>
          <td>{{ item.last_name }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>

export default {
  name: 'Customers',
  props: ['customers'],
}
</script>
<style>
</style>