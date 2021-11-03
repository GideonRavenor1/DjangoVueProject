<template>
<header class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow">
  <a class="navbar-brand col-md-3 col-lg-2 me-0 px-3">DjangoVue</a>
  <div class="navbar-nav">
    <div class="nav-item text-nowrap">
      <router-link to="/profile" class="p-2 text-white user">{{ user.fullName }}</router-link>
      <button class="btn btn-dark logout mb-1"  @click.stop="logout">Sign out</button>
    </div>
  </div>
</header>
</template>

<script>
import axios from "axios";
import {useRouter} from "vue-router";
import {useStore} from "vuex";
import {computed} from "vue";

export default {
  name: "Nav",
  // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  setup() {
    const router = useRouter();
    const store = useStore();

    const user = computed(() => store.state.User.user)

    const logout = async () => {
       await axios.post('users/logout/', {});
       await router.push('/login')
    }

    return {
      user,
      logout,
    }
  }
}
</script>

<style scoped>
.user {
  text-decoration: none;
}

.user:hover {
  opacity: 0.5;
}

.logout {
  color: white;
}
</style>