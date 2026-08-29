<template>
  <Transition name="fade-out">
    <div v-if="!isFinished" class="fixed inset-0 z-[9999] flex flex-col items-center justify-center bg-[#0D0D0D] text-[#F5F0E8]">
      <!-- Ornamental Floral Pattern in Background -->
      <div class="absolute inset-0 floral-overlay opacity-30 pointer-events-none"></div>

      <!-- Gold Monogram / Logo (Minimalist, Frameless) -->
      <div class="relative mb-8 select-none animate-float flex justify-center">
        <img src="/assets/logo-white.png" alt="Logo" class="w-24 h-24 object-contain" />
      </div>

      <!-- Text Loading -->
      <h2 class="font-display text-2xl tracking-[0.2em] uppercase font-light text-[#FFFFFF] mb-2">
        The Wedding of
      </h2>
      <p class="font-serif italic text-lg text-white mb-6">Syifa & Arief</p>

      <!-- Elegant Progress Indicator -->
      <div class="w-48 h-[1px] bg-[#FFFFFF]/20 relative overflow-hidden mb-3">
        <div 
          class="h-full bg-[#FFFFFF] transition-all duration-300 ease-out" 
          :style="{ width: `${progress}%` }"
        ></div>
      </div>
      <span class="font-sans text-xs tracking-widest text-[#F3F4F6] font-light uppercase">{{ progress }}%</span>
    </div>
  </Transition>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const emit = defineEmits(['loaded']);
const progress = ref(0);
const isFinished = ref(false);

const assetsToPreload = [
  '/assets/logo-white.png',
  '/assets/bg-cincin-bw.png',
  '/assets/bg-cover.jpeg',
  '/assets/galeri/Edit 1.jpg',
  '/assets/galeri/Edit 2.jpg',
  '/assets/galeri/Edit 3.jpg',
  '/assets/galeri/Edit 4.jpg',
  '/assets/galeri/YDS04716.jpg',
  '/assets/galeri/YDS04858.jpg',
  '/assets/galeri/YDS04933(2).jpg',
  '/assets/galeri/YDS05147.jpg',
  '/assets/galeri/YDS05318.jpg',
  '/assets/galeri/YDS05364.jpg',
  '/assets/galeri/YDS05386(1).jpg',
  '/assets/qris.png'
];

onMounted(() => {
  let loadedCount = 0;
  const totalAssets = assetsToPreload.length;

  if (totalAssets === 0) {
    simulateProgress();
    return;
  }

  // Preload Images
  assetsToPreload.forEach((src) => {
    const img = new Image();
    img.src = src;
    img.onload = img.onerror = () => {
      loadedCount++;
      const currentTargetProgress = Math.round((loadedCount / totalAssets) * 100);
      animateToProgress(currentTargetProgress);
    };
  });

  // Safe fallback if assets take too long
  setTimeout(() => {
    if (progress.value < 100) {
      animateToProgress(100);
    }
  }, 5000);
});

function animateToProgress(target) {
  const interval = setInterval(() => {
    if (progress.value < target) {
      progress.value++;
    } else {
      clearInterval(interval);
      if (progress.value >= 100) {
        setTimeout(() => {
          isFinished.value = true;
          emit('loaded');
        }, 600);
      }
    }
  }, 10);
}

function simulateProgress() {
  const interval = setInterval(() => {
    if (progress.value < 100) {
      progress.value += 5;
    } else {
      clearInterval(interval);
      setTimeout(() => {
        isFinished.value = true;
        emit('loaded');
      }, 600);
    }
  }, 80);
}
</script>

<style scoped>
.fade-out-leave-active {
  transition: opacity 1s cubic-bezier(0.16, 1, 0.3, 1), transform 1s cubic-bezier(0.16, 1, 0.3, 1);
}
.fade-out-leave-to {
  opacity: 0;
  transform: scale(1.05);
}
</style>

