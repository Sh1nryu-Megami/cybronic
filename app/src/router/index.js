import { createRouter, createWebHistory } from '@ionic/vue-router';

const routes = [
  {
    path: '/',
    redirect: '/home'
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
