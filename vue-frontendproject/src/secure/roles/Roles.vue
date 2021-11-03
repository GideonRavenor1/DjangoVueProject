<template>
  <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
    <div class="btn-toolbar mb-2 mb-md-0" v-if="authenticatedUser.canEdit('users')">
      <router-link to="/roles/create" class="btn btn-sm btn-primary">Add</router-link>
    </div>
  </div>
  <div class="table-responsive w-75">
    <table class="table table-striped table-sm">
      <thead>
      <tr>
        <th scope="col">id</th>
        <th scope="col">Name</th>
        <th scope="col">Action</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="role in roles" :key="role.id">
        <td>{{ role.id }}</td>
        <td>{{ role.name }}</td>
        <td>
          <div class="btn-group mr-2" role="group" aria-label="Basic example" v-if="authenticatedUser.canEdit('users')">
            <router-link :to="`/roles/${role.id}/edit`" class="btn btn-warning">Edit</router-link>
            <button class="btn btn-danger" @click="del(role.id)">Delete</button>
          </div>
        </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script lang="ts">
import axios from "axios";
import {ref, onMounted, computed} from "vue";
import {Entity} from "@/interfaces/entity";
import {Roles} from "@/interfaces/roles";
import {useStore} from "vuex";


interface RolesResponse {
  data: Roles[]
}
export default {
  name: "Roles",
  // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  setup() {
    const store = useStore();
    const authenticatedUser = computed(() => store.state.User.user);

    const roles = ref();
    onMounted(async () => {
      const response = await axios.get<RolesResponse>('users/roles/');
      roles.value = response.data.data;

    })

    const del = async (roleId: number) => {
      if(confirm('Are you sure you want delete this record?')){
        await axios.delete(`users/roles/${roleId}/`);
        roles.value = roles.value.filter((user: Entity) => user.id !== roleId);
      }
    }
    return {
      roles,
      del,
      authenticatedUser
    }
  }
}
</script>
