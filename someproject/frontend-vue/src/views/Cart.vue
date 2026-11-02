<script setup>
import { useRouter } from 'vue-router';
import { useCartStore } from '../stores/cart';

const cartStore = useCartStore();
const router = useRouter();
</script>

<template>
  <div class="container section">
    <h1 class="section-title">Ваша корзина</h1>

  
    <div v-if="cartStore.cart.length === 0" class="empty-cart">
      <h2>В корзине пока пусто</h2>
      <p style="color: var(--text-muted); margin-bottom: 20px;">Самое время выбрать идеальное путешествие.</p>
      <router-link to="/tours" class="btn btn-primary">Перейти к турам</router-link>
    </div>

    <div v-else class="cart-layout">
   
      <div class="cart-items">
        <div v-for="tour in cartStore.cart" :key="tour.id" class="cart-item">
          <img :src="tour.image" :alt="tour.title" class="cart-img" />
          
          <div class="cart-info">
            <h3>{{ tour.title }}</h3>
            <p class="cart-location">{{ tour.country }}, {{ tour.city }}</p>
            <p class="cart-duration"> {{ tour.duration }} дней</p>
          </div>

          <div class="cart-actions">
            <span class="cart-price">{{ tour.price.toLocaleString() }} ₽</span>
            <button class="btn-remove" @click="cartStore.removeFromCart(tour.id)">
              Удалить
            </button>
          </div>
        </div>
      </div>

      <aside class="cart-summary">
        <h3>Итог заказа</h3>
        
        <div class="summary-row">
          <span>Туров в корзине:</span>
          <span>{{ cartStore.cart.length }} шт.</span>
        </div>
        
        <div class="summary-row total-row">
          <span>Общая стоимость:</span>
          <strong>{{ cartStore.totalPrice.toLocaleString() }} ₽</strong>
        </div>

        <button class="btn btn-primary btn-lg checkout-btn" @click="router.push('/checkout')">
          Перейти к оформлению
        </button>
        
        <button class="btn btn-outline clear-btn" @click="cartStore.clearCart()">
          Очистить корзину
        </button>
      </aside>

    </div>
  </div>
</template>