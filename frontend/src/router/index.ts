import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Playground from '../views/Playground.vue'
const routes = [
  { path: '/login', component: Login },
  { path: '/playground', component: Playground}
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router