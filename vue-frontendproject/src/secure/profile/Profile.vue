<template>
  <form class="w-75">
    <h2>Account Information</h2>
    <hr>
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
    <button class="btn btn-success" @click.prevent="submitInfo">Update</button>
  </form>
  <form class="w-75">
    <h2 class="mt-4">Change Password</h2>
    <hr>
    <div class="input-group mb-3 mt-3">
      <input type="password" class="form-control" placeholder="Password" aria-label="Password" name="password" v-model="password">
    </div>
    <div class="input-group mb-3">
      <input type="password" class="form-control" placeholder="Password Confirm"
             aria-label="Password Confirm" name="password_confirm" v-model="passwordConfirm">
    </div>

    <button class="btn btn-warning" @click.prevent="submitPassword">Change Password</button>
  </form>
</template>

<script lang="ts">
import {ref, onMounted, computed} from "vue";
import axios from "axios";
import {Users} from "@/interfaces/users";
import {useStore} from "vuex";
import {User} from "@/classes/user";

interface UserResponse {
  data: Users
}

export default {
  name: "Profile",
  // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  setup() {
    const userName = ref('');
    const email = ref('');
    const firstName = ref('');
    const lastName = ref('');
    const roleId = ref(0);
    const password = ref('');
    const passwordConfirm = ref('');

    const store = useStore()


    onMounted(async () => {
      const user = computed(() => store.state.User.user)
      userName.value = user.value.username;
      firstName.value = user.value.first_name;
      lastName.value = user.value.last_name;
      email.value = user.value.email;
      if (user.value.role === null) {
        roleId.value = 0;
      } else {
        roleId.value = user.value.role.id
      }

    });

    const submitInfo = async () => {
      const response = await axios.put<UserResponse>('users/info/', {
        username: userName.value,
        email: email.value,
        first_name: firstName.value,
        last_name: lastName.value,
        role_id: roleId.value,

      })

      const u: User = response.data.data
      await store.dispatch('User/setUser', new User(
            u.id,
            u.username,
            u.first_name,
            u.last_name,
            u.email,
            u.role,
            u.permissions
        ))
    };

    const submitPassword = async () => {
      await axios.put('users/password/', {
        username: userName.value,
        email: email.value,
        first_name: firstName.value,
        last_name: lastName.value,
        role_id: roleId.value,
        password: password.value,
        password_confirm: passwordConfirm.value
      });
      password.value = '';
      passwordConfirm.value = '';
    }


    return {
      userName,
      email,
      firstName,
      lastName,
      password,
      passwordConfirm,
      submitInfo,
      submitPassword

    }

  }
}
</script>
