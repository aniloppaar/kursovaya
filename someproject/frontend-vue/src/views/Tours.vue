<script setup>
import { ref, computed, onMounted } from 'vue';
import { getTours } from '../api';
import TourCard from '../components/TourCard.vue';

const tours = ref([]);
const loading = ref(true);
const search = ref('');
const selectedCountry = ref('');
const sortBy = ref('');

onMounted(async () => {
  try {
    const res = await getTours();
    tours.value = res.data;
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
});

const countries = computed(() => [...new Set(tours.value.map(t => t.country))]);

const filteredTours = computed(() => {
  let result = [...tours.value];
  
  if (search.value) {
    const q = search.value.toLowerCase();
    result = result.filter(t => 
      t.title.toLowerCase().includes(q) || 
      t.country.toLowerCase().includes(q)
    );
  }
  if (selectedCountry.value) {
    result = result.filter(t => t.country === selectedCountry.value);
  }
  
  if (sortBy.value === 'price') result.sort((a, b) => a.price - b.price);
  if (sortBy.value === '-price') result.sort((a, b) => b.price - a.price);
  if (sortBy.value === '-rating') result.sort((a, b) => b.rating - a.rating);

  return result;
});
</script>

<template>
  <div class="container section">
    <h1 class="section-title">Наши туры</h1>
    
    <div class="filter-bar">
      <input v-model="search" type="text" placeholder="🔍 Поиск тура..." class="input" />
      <select v-model="selectedCountry" class="input">
        <option value="">Все страны</option>
        <option v-for="c in countries" :key="c" :value="c">{{ c }}</option>
      </select>
      <select v-model="sortBy" class="input">
        <option value="">Сортировка</option>
        <option value="price">Цена ↑</option>
        <option value="-price">Цена ↓</option>
        <option value="-rating">По рейтингу</option>
      </select>
    </div>

    <p class="results-count">Найдено туров: {{ filteredTours.length }}</p>

    <div v-if="loading" style="text-align: center; padding: 40px;">Загрузка...</div>
    <div v-else-if="filteredTours.length === 0" class="empty">😕 Ничего не найдено</div>
    <div v-else class="tours-grid">
      <TourCard v-for="tour in filteredTours" :key="tour.id" :tour="tour" />
    </div>
  </div>
</template>