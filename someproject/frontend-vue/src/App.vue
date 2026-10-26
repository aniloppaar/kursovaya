<script setup>
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';
import { useToastStore } from './stores/toast';

const toastStore = useToastStore();
</script>

<template>
  <div class="app">
    <Header />
    <main class="main">
      <router-view />
    </main>
    <Footer />

    <!-- Уведомления -->
    <div class="toast-container">
      <div 
        v-for="t in toastStore.toasts" 
        :key="t.id" 
        :class="['toast', `toast-${t.type}`]"
      >
        {{ t.type === 'success' ? '✅' : '⚠️' }} {{ t.message }}
      </div>
    </div>
  </div>
</template>