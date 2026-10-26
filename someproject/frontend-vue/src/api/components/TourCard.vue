<script setup>
import { computed } from 'vue';
import { useCartStore } from '../stores/cart';

const props = defineProps({ tour: Object });
const cartStore = useCartStore();

const inCart = computed(() => 
  cartStore.cart.find((t) => t.id === props.tour.id)
);
</script>

<template>
  <div class="tour-card">
    <img :src="tour.image" :alt="tour.title" class="tour-image" />
    <div class="tour-body">
      <div class="tour-header">
        <h3>{{ tour.title }}</h3>
        <span class="rating">⭐ {{ tour.rating }}</span>
      </div>
      <p class="tour-location">📍 {{ tour.country }}, {{ tour.city }}</p>
      <p class="tour-desc">{{ tour.description }}</p>
      <div class="tour-footer">
        <span class="price">{{ tour.price.toLocaleString() }} ₽</span>
        <span class="duration"> / {{ tour.duration }} дней</span>
      </div>
      <div class="tour-actions">
        <router-link :to="`/tours/${tour.id}`" class="btn btn-outline">Подробнее</router-link>
        <button 
          :class="['btn', inCart ? 'btn-success' : 'btn-primary']"
          @click="cartStore.addToCart(tour)"
          :disabled="!!inCart"
        >
          {{ inCart ? '✓ В корзине' : 'Забронировать' }}
        </button>
      </div>
    </div>
  </div>
</template>