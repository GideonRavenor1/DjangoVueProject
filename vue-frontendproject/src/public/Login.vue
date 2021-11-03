<template>
  <main class="form-login">
    <form @submit.prevent="submit">
      <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

      <div class="form-floating">
        <input type="text" class="form-control" id="userName" placeholder="Bastard" required v-model="userName">
        <label for="username">Username</label>
      </div>
      <div class="form-floating">
        <input type="password" class="form-control" id="password" placeholder="Password" required v-model="password">
        <label for="password">Password</label>
      </div>

      <button class="w-100 btn btn-lg btn-primary mb-2" type="submit">Sign in</button>

        <router-link to="/register">
          <button class="w-100 btn btn-lg btn-primary">Registration</button></router-link>


      <p class="mt-5 mb-3 text-muted">&copy; 2017–2021</p>
    </form>
  </main>
</template>

<script>
import {ref} from "vue";
import axios from "axios";
import {useRouter} from "vue-router";

export default {
  name: "Login",
  // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  setup() {
    const userName = ref('');
    const password = ref('');
    const router = useRouter();

    const submit = async () => {
      await axios.post('users/login/', {
        username: userName.value,
        password: password.value,
      })

      await router.push('/')
    }
    return {
      userName,
      password,
      submit
    }


  }
}
</script>

<style scoped>
html,
body {
  height: 100%;
}

body {
  display: flex;
  align-items: center;
  text-align: center;
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: #f5f5f5;
}

.form-login {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: auto;
}

.form-login {
  padding: 50px;
  position: fixed; top: 50%; left: 50%;
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}

.form-login .form-floating:focus-within {
  z-index: 2;
}



.form-login #userName,
.form-login #password {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

</style>