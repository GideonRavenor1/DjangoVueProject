<template>
    <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
      <div class="position-sticky pt-3">
        <ul class="nav flex-column">
          <li class="nav-item">
            <router-link to="/dashboard" active-class="active" class="nav-link">
              <button class="btn btn-info">Dashboard</button>
            </router-link>
          </li>
          <li class="nav-item" v-if="user.canView('users')">
            <router-link to="/users" active-class="active" class="nav-link">
               <button class="btn btn-primary">Users</button>
            </router-link>
          </li>
          <li class="nav-item" v-if="user.canView('roles')">
            <router-link to="/roles" active-class="active" class="nav-link">
               <button class="btn btn-success">Roles</button>
            </router-link>
          </li>
          <li class="nav-item" v-if="user.canView('products')">
            <router-link to="/products" active-class="active" class="nav-link">
               <button class="btn btn-success">Products</button>
            </router-link>
          </li>
          <li class="nav-item" v-if="user.canView('orders')">
            <router-link to="/orders" active-class="active" class="nav-link">
               <button class="btn btn-danger">Orders</button>
            </router-link>
          </li>
        </ul>
      </div>
    </nav>
</template>

<script>
import {computed} from 'vue';
import {useStore} from "vuex";
export default {
  name: "Menu",
  // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  setup() {
    const store = useStore();
    const user = computed(() => store.state.User.user);
    return {
      user
    }
  }
}
</script>
