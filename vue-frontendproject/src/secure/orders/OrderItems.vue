<template>
   <div class="table-responsive">
    <table class="table table-striped table-sm">
      <thead>
      <tr>
        <th scope="col">id</th>
        <th scope="col">Product Title</th>
        <th scope="col">Quantity</th>
        <th scope="col">Price</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="item in orderItems" :key="item.id">
        <td>{{ item.id }}</td>
        <td>{{ item.product_title }}</td>
        <td>{{ item.quantity }}</td>
        <td>{{ item.price }}</td>
      </tr>
      </tbody>
    </table>
   </div>

</template>

<script>
import {ref, onMounted} from "vue";
import axios from "axios";
import {useRoute} from "vue-router";

export default {
  name: "OrderItems",
  // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  setup() {
    const {params} = useRoute();
    const orderItems = ref([]);

    onMounted(async () => {
      const response = await axios.get(`orders/order/${params.id}/`);
      orderItems.value = response.data.data.order_items;
    })
    return {
      orderItems
    }
  }
}
</script>

<style scoped>

</style>