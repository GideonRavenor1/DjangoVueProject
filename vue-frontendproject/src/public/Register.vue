<template>
<main class="form-register">
  <form @submit.prevent="submit">
    <h1 class="h3 mb-3 fw-normal">Please register</h1>

    <div class="form-floating">
      <input type="text" class="form-control" id="userName" placeholder="Bastard" required v-model="userName">
      <label for="username">Username</label>
    </div>
    <div class="form-floating">
      <input type="email" class="form-control" id="inputEmail" placeholder="john_snow@example.com" required v-model="email">
      <label for="inputEmail">Email address</label>
    </div>
    <div class="form-floating">
      <input type="text" class="form-control" id="firstName" placeholder="John" required v-model="firstName">
      <label for="firstName">First name</label>
    </div>
    <div class="form-floating">
      <input type="text" class="form-control" id="lastName" placeholder="Snow" required v-model="lastName">
      <label for="lastName">Last name</label>
    </div>
    <div class="form-floating">
      <input type="password" class="form-control" id="password" placeholder="Password" required v-model="password">
      <label for="password">Password</label>
    </div>
    <div class="form-floating">
      <input type="password" class="form-control" id="passwordConfirm" placeholder="Password confirm" required v-model="passwordConfirm">
      <label for="passwordConfirm">Password confirm</label>
    </div>

    <button class="w-100 btn btn-lg btn-primary" type="submit">Register</button>
    <p class="mt-5 mb-3 text-muted">&copy; 2017–2021</p>
  </form>
</main>

</template>

<script>
import {ref} from "vue";
import axios from "axios";
import {useRouter} from "vue-router";

export default {
  name: "Register",
  // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  setup() {
    const userName = ref('');
    const email = ref('');
    const firstName = ref('');
    const lastName = ref('');
    const password = ref('');
    const passwordConfirm = ref('');
    const router = useRouter()


    const submit = async () => {
      await axios.post('users/register/', {
        username: userName.value,
        email: email.value,
        first_name: firstName.value,
        last_name: lastName.value,
        password: password.value,
        password_confirm: passwordConfirm.value,
        role: 3
      });
      await router.push('/login');
    }



    return {
      userName,
      email,
      firstName,
      lastName,
      password,
      passwordConfirm,
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

.form-register {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: auto;
}

.form-register {
  padding: 50px;
  position: fixed; top: 50%; left: 50%;
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}

.form-register .form-floating:focus-within {
  z-index: 2;
}



.form-register #userName, .form-register #inputEmail,
.form-register #firstName, .form-register #lastName,
.form-register #password {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

button {
  margin-top: 10px;
}

</style>