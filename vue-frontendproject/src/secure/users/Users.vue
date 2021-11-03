<template>
  <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
    <div class="btn-toolbar mb-2 mb-md-0" v-if="authenticatedUser.canEdit('users')">
      <router-link to="/users/create" class="btn btn-sm btn-primary">Add</router-link>
    </div>
  </div>
  <div class="table-responsive">
    <table class="table table-striped table-sm">
      <thead>
      <tr>
        <th scope="col">id</th>
        <th scope="col">Username</th>
        <th scope="col">First Name</th>
        <th scope="col">Last Name</th>
        <th scope="col">Email</th>
        <th scope="col">Roles</th>
        <th scope="col">Action</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="user in users" :key="user.id">
        <td>{{ user.id }}</td>
        <td>{{ user.username }}</td>
        <td>{{ user.first_name }}</td>
        <td>{{ user.last_name }}</td>
        <td>{{ user.email }}</td>
        <td>{{ user.role ? user.role.name: 'Role not selected' }}</td>
        <td>
          <div class="btn-group mr-2" role="group" aria-label="Basic example" v-if="authenticatedUser.canEdit('users')">
            <router-link :to="`/users/${user.id}/edit`" class="btn btn-warning">Edit</router-link>
            <button class="btn btn-danger" @click="del(user.id)">Delete</button>
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
import {Users} from "@/interfaces/users";
import Paginator from "@/secure/components/Paginator.vue";
import {useStore} from "vuex";


interface UsersResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: Users[];
}

export default {
  name: "Users",
  components: {Paginator},
  // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  setup() {
    const store = useStore();
    const authenticatedUser = computed(() => store.state.User.user);
    const users = ref();
    const lastPage = ref();

    const load = async (page = 1) => {
      const response = await axios.get<UsersResponse>(`users/?page=${page}`);
      users.value = response.data.results;
      lastPage.value = response.data.next
    }
    const del = async (userId: number) => {
      if(confirm('Are you sure you want delete this record?')){
        await axios.delete(`users/user/${userId}/`);
        users.value = users.value.filter((user: Entity) => user.id !== userId);
      }

    };

    onMounted(load);

    return {
      users,
      del,
      load,
      lastPage,
      authenticatedUser
    }
  }
}
</script>
