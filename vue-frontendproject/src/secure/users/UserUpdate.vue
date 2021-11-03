<template>
  <form class="w-75">
    <div class="input-group mb-3 mt-3">
      <input type="text" class="form-control" placeholder="Username" aria-label="Username" name="username" v-model="userName">
    </div>
    <div class="input-group mb-3">
      <input type="email" class="form-control" placeholder="Email" aria-label="Email" name="email" v-model="email">
      <span class="input-group-text" id="basic-addon2">example@example.com</span>
    </div>
    <div class="input-group mb-3">
      <input type="text" class="form-control" placeholder="First name" aria-label="First name" name="first_name" v-model="firstName">
    </div>
    <div class="input-group mb-3">
      <input type="text" class="form-control" placeholder="Last name" aria-label="Last name" name="last_name" v-model="lastName">
    </div>
    <div class="input-group mb-3">
      <select name="role_id" class="form-control" v-model="roleId">
          <option :value="0">Select role</option>
          <option v-for="role in roles" :key="role.id" :value="role.id">
            {{ role.name}}
          </option>
      </select>
    </div>
    <button class="btn btn-success" @click.prevent="submit">Update</button>
  </form>
</template>

<script lang="ts">
import {ref, onMounted} from "vue";
import axios from "axios";
import {useRouter, useRoute} from "vue-router";
import {User} from "@/classes/user";
import {Roles} from "@/interfaces/roles"
import {Users} from "@/interfaces/users";

interface RolesResponse {
  data: Roles[]
}

interface UserResponse {
  data: Users
}

export default {
  name: "UserUpdate",
  // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  setup() {
    const userName = ref('');
    const email = ref('');
    const firstName = ref('');
    const lastName = ref('');
    const roleId = ref(0);
    const roles = ref();
    const router = useRouter()
    const {params} = useRoute()

    onMounted(async () => {
      const response = await axios.get<RolesResponse>('users/roles/');
      roles.value = response.data.data;

      const userCall = await axios.get<UserResponse>(`users/user/${params.id}/`);

      const user: User = userCall.data.data;
      userName.value = user.username;
      firstName.value = user.first_name;
      lastName.value = user.last_name;
      email.value = user.email;
      if (user.role === null) {
        roleId.value = 0;
      } else {
        roleId.value = user.role.id
      }


  });

    const submit = async () => {
      if(roleId.value === 0) {
        alert('Choose a role');
      } else {
        await axios.put(`users/user/${params.id}/`, {
        username: userName.value,
        email: email.value,
        first_name: firstName.value,
        last_name: lastName.value,
        role_id: roleId.value
      });
        await router.push('/users');
      }
    };

    return {
      userName,
      email,
      firstName,
      lastName,
      roleId,
      roles,
      submit
    }
  }
}
</script>