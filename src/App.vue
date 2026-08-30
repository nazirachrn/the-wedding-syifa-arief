<template>
  <div class="min-h-screen bg-black text-[#F8F9FA] relative selection:bg-white selection:text-black">
    <!-- Top-pinned Silver Scroll Progress Indicator -->
    <div 
      v-if="isUnlocked" 
      class="fixed top-0 left-0 h-1 bg-linear-to-r from-[#D1D5DB] via-[#FFFFFF] to-[#D1D5DB] z-[60] transition-all duration-75"
      :style="{ width: `${scrollProgress}%` }"
    ></div>

    <!-- 1. Loading Screen Preloader -->
    <LoadingScreen @loaded="handleLoaded" />

    <!-- 2. Fullscreen Cover Screen (Locked State) -->
    <CoverScreen @open="handleOpenInvitation" />

    <!-- 3. Core Wedding Content (Rendered only after loading, active when unlocked) -->
    <div :class="['transition-opacity duration-1000 ease-out', isUnlocked ? 'block opacity-100' : 'hidden md:block md:invisible md:h-screen md:overflow-hidden opacity-0']">
      <!-- Main Sections -->
      <HeroSection />
      
      <QuoteSection />
      
      <CoupleSection />
      
      <EventSection />
      
      <GallerySection />
      
      <RSVPSection />
      
      <WishesSection />
      
      <MapSection />
      
      <!-- GiftSection is hidden per user request -->
      <!-- <GiftSection /> -->
      
      <FooterSection />

      <!-- Floating Music Player -->
      <MusicPlayer :shouldPlay="startMusic" />

      <!-- Floating WhatsApp Support Button -->
      <div 
        v-if="isUnlocked"
        class="fixed bottom-6 left-6 z-40 animate-float"
      >
        <a 
          href="https://wa.me/6281277125344?text=Halo%20Syifa%20%26%20Arief%2C%20saya%20ingin%20bertanya%20mengenai%20detail%20acara%20undangan%20pernikahan%20kalian."
          target="_blank"
          class="w-12 h-12 rounded-full bg-[#25D366] shadow-[0_4px_15px_rgba(37,211,102,0.4)] flex items-center justify-center border border-white/40 cursor-pointer transition-all duration-300 hover:scale-110 active:scale-95 group focus:outline-none"
          aria-label="Hubungi via WhatsApp"
        >
          <!-- WhatsApp Custom SVG Logo -->
          <svg 
            class="w-6 h-6 text-white group-hover:scale-110 transition-transform duration-300" 
            fill="currentColor" 
            viewBox="0 0 24 24"
          >
            <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946C.06 5.348 5.397.01 11.966.01c3.178.001 6.169 1.24 8.409 3.485 2.24 2.246 3.475 5.238 3.473 8.417-.006 6.615-5.34 11.952-11.91 11.952-2.001-.002-3.973-.5-5.753-1.447L0 24zm6.59-4.846c1.6.95 3.188 1.449 4.625 1.451 5.403.002 9.792-4.382 9.797-9.779.002-2.614-1.012-5.074-2.858-6.924C16.368 2.053 13.91 1.039 11.3 1.038c-5.41 0-9.796 4.385-9.8 9.782-.001 1.76.46 3.475 1.336 4.993L1.82 21.65l6.059-1.588-.04.025zM17.15 14.19c-.31-.15-1.81-.88-2.09-.98-.28-.1-.48-.15-.68.15-.2.3-.77.98-.95 1.18-.18.2-.35.23-.65.08-1.02-.5-1.92-1.06-2.67-1.72-.51-.44-.92-.95-1.21-1.49-.18-.3-.02-.47.13-.62.14-.14.3-.35.45-.53.15-.18.2-.3.3-.5.1-.2.05-.38-.03-.53-.08-.15-.68-1.63-.93-2.24-.25-.6-.5-.52-.68-.53-.17-.01-.38-.01-.58-.01-.2 0-.53.08-.8.38-.28.3-1.05 1.03-1.05 2.5 0 1.48 1.08 2.9 1.23 3.1.15.2 2.11 3.23 5.13 4.53.72.31 1.28.5 1.72.64.73.23 1.4.2 1.93.12.59-.09 1.81-.74 2.06-1.45.25-.72.25-1.33.18-1.45-.07-.12-.27-.2-.58-.35z"/>
          </svg>
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue';
import LoadingScreen from './components/LoadingScreen.vue';
import CoverScreen from './components/CoverScreen.vue';
import HeroSection from './components/HeroSection.vue';
import QuoteSection from './components/QuoteSection.vue';
import CoupleSection from './components/CoupleSection.vue';
import EventSection from './components/EventSection.vue';
import GallerySection from './components/GallerySection.vue';
import RSVPSection from './components/RSVPSection.vue';
import WishesSection from './components/WishesSection.vue';
import MapSection from './components/MapSection.vue';
import GiftSection from './components/GiftSection.vue';
import FooterSection from './components/FooterSection.vue';
import MusicPlayer from './components/MusicPlayer.vue';

const isLoaded = ref(false);
const isUnlocked = ref(false);
const startMusic = ref(false);
const scrollProgress = ref(0);

// Disable scrolling initially
onMounted(() => {
  document.body.style.overflow = 'hidden';
  window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});

// Loading screen completes preloading
function handleLoaded() {
  isLoaded.value = true;
}

// Buka Undangan is clicked
function handleOpenInvitation() {
  isUnlocked.value = true;
  startMusic.value = true;
  
  // Enable scrolling
  document.body.style.overflow = 'auto';

  // Wait for Vue to update the DOM, then initialize Intersection Observer
  nextTick(() => {
    initScrollAnimations();
    // Trigger initial scroll calculation
    handleScroll();
  });
}

// Calculate scroll progress percentage
function handleScroll() {
  if (!isUnlocked.value) return;
  const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
  const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  scrollProgress.value = height > 0 ? (winScroll / height) * 100 : 0;
}



// Smooth Reveal Animations on Scroll
function initScrollAnimations() {
  const reveals = document.querySelectorAll('.reveal');
  
  if (reveals.length === 0) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('reveal-active');
      }
    });
  }, {
    threshold: 0.02,
    rootMargin: '0px 0px -20px 0px' // Triggers smooth reveal right as element enters view
  });

  reveals.forEach((el) => {
    // Add layout type helper classes before observing
    if (!el.classList.contains('reveal-scale') && !el.classList.contains('reveal-fade')) {
      el.classList.add('reveal-up');
    }
    observer.observe(el);
  });
}
</script>

<style>
/* Reset and body tweaks */
html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  padding: 0;
  background-color: #FAF9F6;
  font-family: 'Poppins', sans-serif;
  overflow-x: hidden;
}
</style>
