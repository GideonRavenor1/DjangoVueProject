import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import Register from '@/public/Register.vue';
import Login from '@/public/Login.vue';
import Secure from '@/secure/Secure.vue';
import Dashboard from '@/secure/dashboard/Dashboard.vue';
import Users from '@/secure/users/Users.vue';
import UserCreate from '@/secure/users/UserCreate.vue';
import UserUpdate from '@/secure/users/UserUpdate.vue';
import Roles from "@/secure/roles/Roles.vue";
import RolesCreate from "@/secure/roles/RolesCreate.vue"
import RolesUpdate from "@/secure/roles/RolesUpdate.vue"
import Products from "@/secure/products/Products.vue"
import ProductsCreate from "@/secure/products/ProductsCreate.vue"
import ProductsUpdate from "@/secure/products/ProductsUpdate.vue"
import Orders from "@/secure/orders/Orders.vue"
import OrderItems from "@/secure/orders/OrderItems.vue"
import Profile from "@/secure/profile/Profile.vue"

const routes: Array<RouteRecordRaw> = [
  {
    path: '/register',
    component: Register
  },
  {
    path: '/login',
    component: Login
  },
  {
    path: '',
    component: Secure,
    children: [
      {
        path: '/',
        redirect: '/dashboard'
      },
      {
        path: '/dashboard',
        component: Dashboard
      },
      {
        path: '/profile',
        component: Profile
      },
      {
        path: '/users',
        component: Users
      },
      {
        path: '/users/create',
        component: UserCreate
      },
      {
        path: '/users/:id/edit',
        component: UserUpdate
      },
      {
        path: '/roles',
        component: Roles
      },
      {
        path: '/roles/create',
        component: RolesCreate
      },
      {
        path: '/roles/:id/edit',
        component: RolesUpdate
      },
      {
        path: '/products',
        component: Products
      },
      {
        path: '/products/create',
        component: ProductsCreate
      },
      {
        path: '/products/:id/edit',
        component: ProductsUpdate
      },
      {
        path: '/orders',
        component: Orders
      },
      {
        path: '/orders/:id',
        component: OrderItems
      },

    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
