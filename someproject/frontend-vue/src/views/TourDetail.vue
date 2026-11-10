<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { getTourById } from '../api';
import { useCartStore } from '../stores/cart';
import { useToastStore } from '../stores/toast';

const route = useRoute();
const router = useRouter();
const cartStore = useCartStore();
const toastStore = useToastStore();

const tour = ref(null);
const loading = ref(true);

onMounted(async () => {
  try {
    const res = await getTourById(route.params.id);
    tour.value = res.data;
  } catch (error) {
    console.error('Ошибка загрузки тура:', error);
    toastStore.showToast('Тур не найден', 'error');
    router.push('/tours');
  } finally {
    loading.value = false;
  }
});

const handleBook = () => {
  if (tour.value) {
    cartStore.addToCart(tour.value);
    toastStore.showToast('Тур добавлен в корзину!', 'success');
  }
};
</script>

<template>
  <div class="container section">
    <div v-if="loading" style="text-align: center; padding: 100px; color: var(--text-muted);">
      Загрузка данных о туре...
    </div>

    <div v-else-if="tour" class="tour-detail-wrapper">
      <button class="back-link" @click="router.back()">
        &larr; Назад к турам
      </button>

      <div class="tour-detail-grid">
        <div class="tour-image-col">
          <img :src="tour.image" :alt="tour.title" class="detail-image" />
        </div>

        <div class="tour-info-col">
          <div class="tour-header">
            <span class="tour-category">{{ tour.category }}</span>
            <span class="tour-rating">⭐ {{ tour.rating }}</span>
          </div>
          
          <h1>{{ tour.title }}</h1>
          <p class="tour-location">📍 {{ tour.country }}, {{ tour.city }}</p>
          
          <div class="tour-description">
            <p>{{ tour.description }}</p>
          </div>

          <div class="tour-itinerary" v-if="tour.program && tour.program.length > 0">
            <h3>Программа тура</h3>
            <div class="itinerary-content">
              <p v-for="day in tour.program" :key="day.id">
                <strong>День {{ day.day_number }}:</strong> {{ day.title }}. {{ day.description }}
              </p>
            </div>
          </div>

          <template v-if="tour.details">
            <div class="tour-hotel" v-if="tour.details.hotel_info">
              <h3>Варианты размещения</h3>
              <p v-for="(line, index) in tour.details.hotel_info.split('\n')" :key="index">
                🏨 {{ line }}
              </p>
            </div>

            <div class="tour-includes" v-if="tour.details.included">
              <h3>Что включено в стоимость:</h3>
              <ul class="include-list">
                <li v-for="(item, index) in tour.details.included.split('\n')" :key="'inc-'+index">
                  <span class="check-icon">✓</span> {{ item }}
                </li>
              </ul>
            </div>

            <div class="tour-excludes" v-if="tour.details.not_included">
              <h3>Оплачивается отдельно:</h3>
              <ul class="exclude-list">
                <li v-for="(item, index) in tour.details.not_included.split('\n')" :key="'exc-'+index">
                  <span class="cross-icon">✕</span> {{ item }}
                </li>
              </ul>
            </div>

            <div class="tour-important" v-if="tour.details.important_info">
              <h3>Важная информация</h3>
              <p v-for="(line, index) in tour.details.important_info.split('\n')" :key="index">
                ℹ️ {{ line }}
              </p>
            </div>
          </template>

          <div class="tour-booking-box">
            <div class="price-box">
              <span class="price-label">Стоимость</span>
              <span class="price-value">{{ tour.price.toLocaleString() }} ₽</span>
            </div>
            <button 
              class="btn btn-primary btn-lg" 
              @click="handleBook"
              :disabled="cartStore.cart.some(t => t.id === tour.id)"
            >
              {{ cartStore.cart.some(t => t.id === tour.id) ? 'Уже в корзине' : 'Забронировать' }}
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>