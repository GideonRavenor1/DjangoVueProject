<template>
 <nav aria-label="Page navigation example">
    <ul class="pagination">
      <li class="page-item">
        <button class="page-link" aria-label="Previous" @click="previous">
          <span aria-hidden="true">Previous</span>
        </button>
      </li>
      <li class="page-item">
        <button class="page-link"  aria-label="Next" @click="next">
          <span aria-hidden="true">Next</span>
        </button>
      </li>
    </ul>
  </nav>
</template>

<script>
import {ref} from "vue";

export default {
  name: "Paginator",
  emits: ['page-changed'],
  props: {
    lastPage: String
  },
  // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  setup(props, {emit}) {
    const page = ref(1)
     const next = async () => {
      if(props.lastPage === null) return;
      page.value += 1;
      emit('page-changed', page.value)

    };
    const previous = async () => {
      if (page.value === 1) return;
      page.value -= 1;
      emit('page-changed', page.value)

    };
    return {
      next,
      previous
    }
  }
}
</script>

<style scoped>

</style>