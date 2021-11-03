<template>
  <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
    <div class="btn-toolbar mb-2 mb-md-0" v-if="authenticatedUser.canEdit('users')">
      <router-link to="/products/create" class="btn btn-sm btn-primary">Add</router-link>
    </div>
  </div>
  <div class="table-responsive">
    <table class="table table-striped table-sm">
      <thead>
      <tr>
        <th scope="col">id</th>
        <th scope="col">Image</th>
        <th scope="col">Title</th>
        <th scope="col">Description</th>
        <th scope="col">Price</th>
        <th scope="col">Action</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="product in products" :key="product.id">
        <td>{{ product.id }}</td>
        <td><img :src="product.image"  height="50" alt="image"/></td>
        <td>{{ product.title }}</td>
        <td>{{ product.description }}</td>
        <td>{{ product.price }}</td>
        <td>
          <div class="btn-group mr-2" role="group" aria-label="Basic example" v-if="authenticatedUser.canEdit('users')">
            <router-link :to="`/products/${product.id}/edit`" class="btn btn-warning">Edit</router-link>
            <button class="btn btn-danger" @click="del(product.id)">Delete</button>
          </div>
        </td>
      </tr>
      </tbody>
    </table>
  </div>
  <Paginator :last-page="lastPage" @page-changed="load($event)"/>
</template>

<script lang="ts">
import {ref, onMounted, computed} from "vue";
import axios from "axios";
import {Entity} from "@/interfaces/entity";
import {Products} from "@/interfaces/products";
import Paginator from "@/secure/components/Paginator.vue";
import {useStore} from "vuex";

interface ProductsResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: Products[]
}

export default {
  name: "Products",
  components: {Paginator},
  // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  setup() {
    const store = useStore();
    const authenticatedUser = computed(() => store.state.User.user);

    const products = ref();
    const lastPage = ref();

    const load = async (page = 1) => {
      const response = await axios.get<ProductsResponse>(`products/?page=${page}`)
      lastPage.value = response.data.next
      products.value = response.data.results;
    };

    onMounted(load);

    const del = async (productId: number) => {
      if(confirm('Are you sure you want delete this record?')){
        await axios.delete(`products/product/${productId}/`);
        products.value = products.value.filter((user: Entity) => user.id !== productId);
      }

    };

    return {
      products,
      del,
      lastPage,
      load,
      authenticatedUser

    }

  }
}
</script>
