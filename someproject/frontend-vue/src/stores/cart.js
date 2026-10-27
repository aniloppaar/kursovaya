import { defineStore } from 'pinia';
import { ref, computed, watch } from 'vue';

export const useCartStore = defineStore('cart', () => {
  const cart = ref(JSON.parse(localStorage.getItem('cart')) || []);

  // Сохраняем в localStorage при каждом изменении
  watch(cart, (newVal) => {
    localStorage.setItem('cart', JSON.stringify(newVal));
  }, { deep: true });

  const totalPrice = computed(() => 
    cart.value.reduce((sum, t) => sum + t.price, 0)
  );

  const addToCart = (tour) => {
    if (!cart.value.find((t) => t.id === tour.id)) {
      cart.value.push(tour);
    }
  };

  const removeFromCart = (id) => {
    cart.value = cart.value.filter((t) => t.id !== id);
  };

  const clearCart = () => {
    cart.value = [];
  };

  return { cart, totalPrice, addToCart, removeFromCart, clearCart };
});