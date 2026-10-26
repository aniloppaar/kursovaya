<script setup>
import { ref } from 'vue';
import { useCartStore } from '../stores/cart';

const cartStore = useCartStore();
const isMenuOpen = ref(false);
</script>

<template>
  <header class="header">
    <div class="container header-inner">
      <router-link to="/" class="logo">✈️ TravelDream</router-link>
      
      <button class="burger" @click="isMenuOpen = !isMenuOpen">
        {{ isMenuOpen ? '✕' : '☰' }}
      </button>

      <nav :class="['nav', { open: isMenuOpen }]" @click="isMenuOpen = false">
        <router-link to="/">Главная</router-link>
        <router-link to="/tours">Туры</router-link>
        <router-link to="/about">О нас</router-link>
        <router-link to="/cart" class="cart-link">
          🛒 Корзина
          <span v-if="cartStore.cart.length > 0" class="badge">
            {{ cartStore.cart.length }}
          </span>
        </router-link>
      </nav>
    </div>
  </header>
</template>