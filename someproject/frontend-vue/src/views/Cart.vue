<script setup>
import { useRouter } from 'vue-router';
import { useCartStore } from '../stores/cart';

const cartStore = useCartStore();
const router = useRouter();
</script>

<template>
  <div class="container section">
    <h1 class="section-title">Корзина</h1>
    
    <div v-if="cartStore.cart.length === 0" class="empty-cart">
      <h2>🛒 Корзина пуста</h2>
      <router-link to="/tours" class="btn btn-primary">Перейти к турам</router-link>
    </div>

    <template v-else>
      <div class="cart-list">
        <div v-for="tour in cartStore.cart" :key="tour.id" class="cart-item">
          <img :src="tour.image" :alt="tour.title" />
          <div class="cart-item-info">
            <h3>{{ tour.title }}</h3>
            <p>📍 {{ tour.country }}, {{ tour.city }}</p>
            <p>🗓️ {{ tour.duration }} дней</p>
          </div>
          <div class="cart-item-right">
            <span class="price">{{ tour.price.toLocaleString() }} ₽</span>
            <button class="btn btn-danger btn-sm" @click="cartStore.removeFromCart(tour.id)">
              Удалить
            </button>
          </div>
        </div>
      </div>

      <div class="cart-total">
        <h2>Итого: {{ cartStore.totalPrice.toLocaleString() }} ₽</h2>
        <div class="cart-total-actions">
          <button class="btn btn-outline" @click="cartStore.clearCart()">Очистить</button>
          <button class="btn btn-primary btn-lg" @click="router.push('/checkout')">
            Оформить заказ →
          </button>
        </div>
      </div>
    </template>
  </div>
</template>