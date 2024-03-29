import { createRouter, createWebHashHistory } from 'vue-router';

const routes = [
  { path: '/', component: () => import ('../views/Files.vue') },
  { path: '/login', component: () => import('../views/Login.vue') }
]


const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;