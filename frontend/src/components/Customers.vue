<template>
  <div>
    <div class="container">
      <form action="">
        <div class="form-group">
          <label for="first_name">Nome</label>
          <input class="form-control" v-model="first_name">
        </div>
        <div class="form-group">
          <label for="last_name">Sobrenome</label>
          <input class="form-control" v-model="last_name">
        </div>
      </form>
    </div>
    <button class="btn btn-primary mb-3">Salvar</button>
    <hr>
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
  props: ['customers', 'first_name', 'last_name'],
}
</script>
<style scoped>
.table {
  border-collapse: collapse;
  width: 30%;
  margin-left: auto;
  margin-right: auto;
}

thead th {
  border-bottom: 2px solid #ddd;
}

tbody th,
td {
  border-bottom: 1px solid #ddd;
}

th,
td {
  padding: 15px;
  text-align: left;
}

tbody tr:hover {
  background-color: #f5f5f5;
}

tfoot tr {
  border-top: 2px solid #ddd;
}
</style>