<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useCartStore } from '../stores/cart';
import { useToastStore } from '../stores/toast';
import { createBooking } from '../api';

const cartStore = useCartStore();
const toastStore = useToastStore();
const router = useRouter();

const form = ref({
  lastName: '', firstName: '', email: '', phone: '',
  passport: '', birthDate: '', travelers: 1,
});

const loading = ref(false);
const bookingNum = ref(null);

const handleSubmit = async () => {
  if (cartStore.cart.length === 0) {
    return toastStore.showToast('Корзина пуста', 'error');
  }

  loading.value = true;
  try {
    const res = await createBooking({
      tour: cartStore.cart[0].id,
      customer_name: `${form.value.lastName} ${form.value.firstName}`,
      email: form.value.email,
      phone: form.value.phone,
      travelers_count: form.value.travelers,
    });
    
    bookingNum.value = res.data.booking_number || 'TD-OK';
    cartStore.clearCart();
    toastStore.showToast('Бронь успешно создана!', 'success');
  } catch (error) {
    console.error(error);
    toastStore.showToast('Ошибка при отправке на сервер', 'error');
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <div class="container section">
    <div v-if="bookingNum" class="success-screen" style="text-align: center;">
      <h1>🎉 Успешно!</h1>
      <p>Ваш номер брони: <strong class="booking-num">{{ bookingNum }}</strong></p>
      <p>Менеджер свяжется с вами в течение 15 минут.</p>
      <button @click="router.push('/')" class="btn btn-primary" style="margin-top: 20px;">На главную</button>
    </div>

    <div v-else-if="cartStore.cart.length === 0" style="text-align: center;">
      <h2>Корзина пуста</h2>
      <router-link to="/tours" class="btn btn-primary">К турам</router-link>
    </div>

    <template v-else>
      <h1 class="section-title">Оформление заказа</h1>
      <div class="checkout-layout">
        <form class="checkout-form" @submit.prevent="handleSubmit">
          <h3>Контактные данные</h3>
          <input v-model="form.lastName" class="input" placeholder="Фамилия" required />
          <input v-model="form.firstName" class="input" placeholder="Имя" required />
          <input v-model="form.email" class="input" type="email" placeholder="E-mail" required />
          <input v-model="form.phone" class="input" placeholder="Телефон" required />
          
          <h3 style="margin-top: 20px;">Данные туриста</h3>
          <input v-model="form.passport" class="input" placeholder="Серия и номер паспорта" required />
          <input v-model="form.birthDate" class="input" type="date" required />
          
          <div style="margin-top: 20px;">
            <label>Количество туристов: </label>
            <input v-model="form.travelers" class="input" type="number" min="1" max="6" />
          </div>

          <button type="submit" class="btn btn-primary btn-lg" style="width: 100%; margin-top: 30px;" :disabled="loading">
            {{ loading ? 'Отправка...' : `Забронировать за ${cartStore.totalPrice.toLocaleString()} ₽` }}
          </button>
        </form>

        <aside class="checkout-aside">
          <h3>Ваш заказ</h3>
          <div v-for="t in cartStore.cart" :key="t.id" style="border-bottom: 1px solid #eee; padding: 10px 0;">
            <p><strong>{{ t.title }}</strong></p>
            <p style="color: #666; font-size: 14px;">{{ t.price.toLocaleString() }} ₽</p>
          </div>
          <h4 style="margin-top: 20px;">Итого: {{ cartStore.totalPrice.toLocaleString() }} ₽</h4>
        </aside>
      </div>
    </template>
  </div>
</template>