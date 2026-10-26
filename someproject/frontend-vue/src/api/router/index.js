import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Tours from '../views/Tours.vue';
import TourDetail from '../views/TourDetail.vue';
import About from '../views/About.vue';
import Cart from '../views/Cart.vue';
import Checkout from '../views/Checkout.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/tours', component: Tours },
  { path: '/tours/:id', component: TourDetail },
  { path: '/about', component: About },
  { path: '/cart', component: Cart },
  { path: '/checkout', component: Checkout },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;