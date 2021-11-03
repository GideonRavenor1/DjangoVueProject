<template>
  <form class="w-75">
    <div class="input-group mb-3 mt-3">
      <input type="text" class="form-control" placeholder="Title" aria-label="Title" name="title" v-model="title">
    </div>
    <div class="input-group mb-3">
      <input type="text" class="form-control" placeholder="Description" aria-label="Description" name="description"
             v-model="description">

    </div>
    <div class="input-group mb-3">
      <input type="text" class="form-control" placeholder="Image" aria-label="Image" name="image" v-model="image">
      <div class="input-group-append">
        <ImageUpload @file-uploaded="image = $event"/>
      </div>
    </div>
    <div class="input-group mb-3">
      <span class="input-group-text">$</span>
      <input type="text" class="form-control" placeholder="Price" aria-label="Price" name="price" v-model="price">
      <span class="input-group-text">.00</span>
    </div>
    <button class="btn btn-success" @click.prevent="submit">Update</button>
  </form>

</template>

<script lang="ts">
import ImageUpload from "@/secure/components/ImageUpload.vue";
import {ref, onMounted} from "vue";
import {useRoute, useRouter} from "vue-router";
import axios from "axios";
import {Product} from "@/classes/product";
import {Products} from "@/interfaces/products";

interface ProductResponse {
  data: Products
}

export default {
  name: "ProductsUpdate",
  components: {ImageUpload},
  // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  setup() {
    const title = ref('');
    const description = ref('');
    const image = ref('');
    const price = ref();
    const router = useRouter();
    const {params} = useRoute();

    onMounted(async () => {
      const response = await axios.get<ProductResponse>(`products/product/${params.id}/`);

      const product: Product = response.data.data

      title.value = product.title;
      description.value = product.description;
      image.value = product.image;
      price.value = product.price;
    })



    const submit = async () => {
      let checkPrice = Number(price.value.split(' ').join(''));
      if (isNaN(checkPrice)) {
        alert('Invalid price format');
      } else {
        await axios.put(`products/product/${params.id}/`, {
          title: title.value,
          description: description.value,
          image: image.value,
          price: checkPrice.toFixed(2)
        })
        await router.push('/products');
      }
    }

    return {
      title,
      description,
      image,
      price,
      submit,
    }
  }
}
</script>

