<template>
  <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
    <div class="btn-toolbar mb-2 mb-md-0"  v-if="authenticatedUser.canEdit('users')">
      <button class="btn btn-sm btn-primary" @click="exportFile">Export</button>
    </div>
  </div>
   <div class="table-responsive">
    <table class="table table-striped table-sm">
      <thead>
      <tr>
        <th scope="col">id</th>
        <th scope="col">First Name</th>
        <th scope="col">Last Name</th>
        <th scope="col">Email</th>
        <th scope="col">Total</th>
        <th scope="col">Action</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="order in orders" :key="order.id">
        <td>{{ order.id }}</td>
        <td>{{ order.first_name }}</td>
        <td>{{ order.last_name }}</td>
        <td>{{ order.email }}</td>
        <td>{{ order.total ? order.total: 'The price is being formed' }}</td>
        <td>
          <div class="btn-group mr-2" role="group" aria-label="Basic example"  v-if="authenticatedUser.canEdit('users')">
            <router-link :to="`/orders/${order.id}`" class="btn btn-warning">View</router-link>
          </div>
        </td>
      </tr>
      </tbody>
    </table>
   </div>
  <Paginator :last-page="lastPage" @page-changed="load($event)" />

</template>

<script>
import Paginator from "../components/Paginator";
import {ref, onMounted, computed} from "vue";
import axios from "axios";
import {useStore} from "vuex";

export default {
  name: "Orders",
  components: {Paginator},
  // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  setup() {
    const store = useStore();
    const authenticatedUser = computed(() => store.state.User.user);

    const orders = ref([]);
    const lastPage = ref();
    const load = async (page = 1) => {
      const response = await axios.get(`orders/?page=${page}`);
      orders.value = response.data.results;
      lastPage.value = response.data.next
    }
    onMounted(load)
    const exportFile = async () => {
      const response = await axios.get('orders/export/', {responseType: 'blob'});
      new Blob([response.data], {type: 'text/csv'});
      const downloadURL = window.URL.createObjectURL(response.data);
      const link = document.createElement('a');
      link.href = downloadURL;
      link.download = 'orders.csv';
      link.click();

    }
    return {
      lastPage,
      load,
      orders,
      exportFile,
      authenticatedUser
    }


  }
}
</script>

<style scoped>

</style>