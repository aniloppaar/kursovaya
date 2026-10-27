<script setup>
import { ref, onMounted } from 'vue';
import { getTours } from '../api';
import TourCard from '../components/TourCard.vue';

const tours = ref([]);
const loading = ref(true);

// Блок с направлениями для красоты
const destinations = [
  { title: 'Европа', count: '24 тура', image: 'https://images.unsplash.com/photo-1499856871958-5b9627545d1a?w=600' },
  { title: 'Азия', count: '18 туров', image: 'https://images.unsplash.com/photo-1528181304800-259b08848526?w=600' },
  { title: 'Ближний Восток', count: '12 туров', image: 'https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=600' },
];

onMounted(async () => {
  try {
    const res = await getTours();
    tours.value = res.data.slice(0, 3); // Берем 3 тура
  } catch (error) {
    console.error("Ошибка при загрузке туров:", error);
  } finally {
    loading.value = false;
  }
});
</script>

<template>
  <div>

    <section class="hero" style="
      background: linear-gradient(rgba(255,255,255,0.6), rgba(255,255,255,0.8)), 
                  url('https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?w=1920') center/cover;
      padding: 220px 0;
    ">
      <div class="container hero-content">
        <span class="hero-label">Новый взгляд на путешествия</span>
        <h1 style="color: var(--text-main);">Искусство путешествовать</h1>
        <p style="color: var(--text-main);">Продуманные маршруты, скрытые жемчужины и премиальный отдых для тех, кто ценит свое время.</p>
        <router-link to="/tours" class="btn btn-primary btn-lg mt-4">
          Исследовать направления
        </router-link>
      </div>
    </section>

    <!-- ПОПУЛЯРНЫЕ ТУРЫ -->
    <section class="container section">
      <div class="section-header">
        <h2 class="section-title">Избранные маршруты</h2>
        <router-link to="/tours" class="view-all">Смотреть все туры &rarr;</router-link>
      </div>
      
      <div v-if="loading" style="text-align: center; padding: 40px; color: var(--text-muted);">
        Загрузка направлений...
      </div>
      <div v-else-if="tours.length === 0" style="text-align: center; padding: 40px; color: var(--text-muted);">
        Туры пока не добавлены. Пожалуйста, проверьте базу данных.
      </div>
      <div v-else class="tours-grid">
        <TourCard v-for="tour in tours" :key="tour.id" :tour="tour" />
      </div>
    </section>

    <!-- БЛОК С РЕГИОНАМИ -->
    <section class="container section" style="background-color: var(--bg-secondary); padding: 80px 40px; border-radius: var(--radius);">
      <h2 class="section-title">География путешествий</h2>
      <div class="destinations-grid">
        <div v-for="dest in destinations" :key="dest.title" class="destination-card">
          <img :src="dest.image" :alt="dest.title" class="dest-image" />
          <div class="dest-info">
            <h3>{{ dest.title }}</h3>
            <p>{{ dest.count }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ФИЛОСОФИЯ КОМПАНИИ (Вместо скучных фич) -->
    <section class="container section philosophy-section">
      <div class="philosophy-text">
        <h2>Почему TravelDream?</h2>
        <p>Мы не просто продаем туры. Мы создаем впечатления. Каждый наш маршрут — это результат работы экспертов, которые лично посетили эти места.</p>
        <ul class="philosophy-list">
          <li><span>01</span> Индивидуальный подход к каждому клиенту</li>
          <li><span>02</span> Только проверенные отели и гиды</li>
          <li><span>03</span> Поддержка 24/7 на всех этапах</li>
        </ul>
      </div>
      <div class="philosophy-image">
        <img src="https://images.unsplash.com/photo-1530789253388-582c481c54b0?w=800" alt="Путешествия" />
      </div>
    </section>
  </div>
</template>