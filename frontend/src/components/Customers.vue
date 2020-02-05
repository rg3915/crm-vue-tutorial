<template>
  <div>
    <div class="container">
      <form action="">
        <div class="form-group">
          <label for="username">Usuário</label>
          <input class="form-control" v-model="username">
        </div>
        <div class="form-group">
          <label for="first_name">Nome</label>
          <input class="form-control" v-model="first_name">
        </div>
        <div class="form-group">
          <label for="last_name">Sobrenome</label>
          <input class="form-control" v-model="last_name">
        </div>
        <div class="form-group">
          <label for="email">E-mail</label>
          <input type='email' class="form-control" v-model="email">
        </div>
      </form>
    </div>
    <button class="btn btn-primary mb-3" @click="saveCustomer">Salvar</button>
    <hr>
    <h1>Clientes</h1>
    <table class="table">
      <thead>
        <tr>
          <th>Usuário</th>
          <th>Nome</th>
          <th>Sobrenome</th>
          <th>E-mail</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in customers" :key="item.id">
          <td>{{ item.username }}</td>
          <td>{{ item.first_name }}</td>
          <td>{{ item.last_name }}</td>
          <td>{{ item.email }}</td>
          <td>
            <button @click="editCustomer(item)">Editar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

const endpoint = 'http://localhost:8000'

export default {
  name: 'Customers',
  data() {
    return {
      customers: [],
      username: '',
      first_name: '',
      last_name: '',
      email: '',
    }
  },
  created() {
    axios.get(endpoint + '/api/customers/')
      .then(response => {
        this.customers = response.data.data
      })
  },
  methods: {
    saveCustomer() {
      let bodyFormData = new FormData();
      bodyFormData.append('username', this.username);
      bodyFormData.append('first_name', this.first_name);
      bodyFormData.append('last_name', this.last_name);
      bodyFormData.append('email', this.email);

      axios.post(endpoint + '/api/customers/add/', bodyFormData)
        .then(response => {
          this.customers.push(response.data.data)
        })
    },
    editCustomer(item) {
      this.username = item.username
      this.first_name = item.first_name
      this.last_name = item.last_name
      this.email = item.email
    }
  }
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